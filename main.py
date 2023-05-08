from EdgeGPT import Chatbot
from aiohttp import web
import time
import random
import string
import json

PORT = 8081
HOST = "127.0.0.1"

def prepare_response(*json_objects):
    response = b""

    for obj in json_objects:
        if isinstance(obj, str):
            if obj == "DONE":
                response += b"data: " + b"[DONE]" + b"\n\n"
                continue

        response += b"data: " + json.dumps(obj).encode() + b"\n\n"

    return response


def transform_message(message):
    role = message["role"]
    content = message["content"]
    anchor = "#additional_instructions" if role == "system" else "#message"
    return f"[{role}]({anchor})\n{content}\n\n"


def process_messages(messages):
    transformed_messages = [transform_message(message) for message in messages]
    return "".join(transformed_messages)+"\n"


def response_data(id, created, content):
    return {
        "id": id,
        "created": created,
        "object": "chat.completion",
        "model": "gpt-4",
        "choices": [{
            "message": {
                "role": 'assistant',
                "content": content
            },
            'finish_reason': 'stop',
            'index': 0,
        }]
    }


class SSEHandler(web.View):

    id = "chatcmpl-" + ''.join(random.choices(string.ascii_letters + string.digits, k=29))
    created = str(int(time.time()))

    async def get(self):
        data = {
                   "object": "list",
                   "data": [
                       {
                        "id": "gpt-4",
                        "object": "model",
                        "created": self.created,
                        "owned_by": "OpenAI",
                        "permissions": [],
                        "root": 'gpt-4',
                        "parent": None
                       }
                   ]
               }

        # Return JSON response
        return web.json_response(data)

    async def post(self):
        request_data = await self.request.json()

        messages = request_data.get('messages', [])
        prompt = messages[-1]['content']
        context = process_messages(messages[:-1])
        stream = request_data.get('stream', [])
        if stream:
            self.response = web.StreamResponse(
                status=200,
                headers={
                    'Content-Type': 'application/json',
                }
            )
            await self.response.prepare(self.request)
        else:
            self.response = web.StreamResponse(
                status=200,
                headers={
                    'Content-Type': 'application/json',
                }
            )
            await self.response.prepare(self.request)

        conversation_style = self.request.path.split('/')[1]
        if conversation_style not in ["creative", "balanced", "precise"]:
            conversation_style = "creative"

        suggestion = self.request.path.split('/')[2]
        if suggestion != "suggestion":
            suggestion = None
        try:
            chatbot = await Chatbot.create(cookie_path="cookies.json")
        except Exception as e:
            if str(e) == "[Errno 11001] getaddrinfo failed":
                print("Нет интернет соединения.")
                return
            print("Ошибка запуска чатбота.", str(e))
            return
        end_data = {
            "id": self.id,
            "object": "chat.completion.chunk",
            "created": self.created,
            "model": "gpt-4",
            "choices": [
                {
                    "delta": {},
                    "index": 0,
                    "finish_reason": "stop"
                }
            ]
        }

        filtered_data = {
            "id": self.id,
            "object": "chat.completion.chunk",
            "created": self.created,
            "model": "gpt-4",
            "choices": [
                {
                    "delta": {
                        "content": "Отфильтровано."
                    },
                    "index": 0,
                    "finish_reason": "null"
                }
            ]
        }

        async def output():
            non_stream_response = ""
            wrote = 0
            async for final, response in chatbot.ask_stream(
                    prompt=prompt,
                    raw=True,
                    webpage_context=context,
                    conversation_style=conversation_style,
                    search_result=True,
            ):

                if not final and response["type"] == 1 and "messages" in response["arguments"][0]:
                    message = response["arguments"][0]["messages"][0]
                    match message.get("messageType"):
                        case None:
                            if "cursor" in response["arguments"][0]:
                                print("Ответ от сервера:\n")
                                wrote = 0
                            if message.get("contentOrigin") == "Apology":
                                if stream and wrote == 0:
                                    await self.response.write(prepare_response(filtered_data))

                                if stream:
                                    await self.response.write(prepare_response(end_data, "DONE"))
                                else:
                                    await self.response.write(
                                        json.dumps(
                                            response_data(
                                                self.id,
                                                self.created,
                                                non_stream_response
                                            )
                                        ).encode()
                                    )
                                print("\nСообщение отозвано.")
                                break
                            else:
                                data = {
                                    "id": self.id,
                                    "object": "chat.completion.chunk",
                                    "created": self.created,
                                    "model": "gpt-4",
                                    "choices": [
                                        {
                                            "delta": {
                                                "content": message['text'][wrote:]
                                            },
                                                "index": 0,
                                                "finish_reason": "null"
                                        }
                                    ]
                                }
                                if stream:
                                    await self.response.write(prepare_response(data))
                                else:
                                    non_stream_response += message['text'][wrote:]
                                print(message["text"][wrote:], end="")
                                wrote = len(message["text"])
                                if "suggestedResponses" in message:
                                    suggested_responses = '\n'.join(x["text"] for x in message["suggestedResponses"])
                                    #suggested_responses = "\n```\n" + suggested_responses + "\n```"
                                    suggested_responses = "\n```" + suggested_responses + "```"
                                    if stream:
                                        data = {
                                            "id": self.id,
                                            "object": "chat.completion.chunk",
                                            "created": self.created,
                                            "model": "gpt-4",
                                            "choices": [
                                                {
                                                    "delta": {
                                                        "content": suggested_responses
                                                    },
                                                    "index": 0,
                                                    "finish_reason": "null"
                                                }
                                            ]
                                        }
                                        if suggestion:
                                            await self.response.write(prepare_response(data, end_data, "DONE"))
                                        else:
                                            await self.response.write(prepare_response(end_data, "DONE"))
                                    else:
                                        if suggestion:
                                            non_stream_response = non_stream_response + suggested_responses
                                        await self.response.write(
                                            json.dumps(
                                                response_data(
                                                    self.id,
                                                    self.created,
                                                    non_stream_response
                                                )
                                            ).encode()
                                        )
                                    break
                if final and not response["item"]["messages"][-1].get("text"):
                    if stream:
                        await self.response.write(prepare_response(filtered_data, end_data))
                    print("Сработал фильтр.")

        try:
            await output()
        except Exception as e:
            if(str(e) == "'messages'"):
                print("Ошибка:", str(e), "\nПроблема с учеткой. Либо забанили, либо нужно залогиниться.")
            if(str(e) == " " or str(e) == ""):
                print("Таймаут.")
            else:
                print("Ошибка: ", str(e))
        await chatbot.close()

        return self.response


app = web.Application()
app.router.add_routes([
    web.route('*', '/{tail:.*}', SSEHandler),
])

if __name__ == '__main__':
    print(f"Есть несколько режимов (разнятся температурой):\n"
          f"По дефолту стоит creative: http://{HOST}:{PORT}/\n"
          f"Режим creative: http://{HOST}:{PORT}/creative\n"
          f"Режим precise:  http://{HOST}:{PORT}/precise\n"
          f"Режим balanced: http://{HOST}:{PORT}/balanced\n"
          f"Также есть режим подсказок. Чтобы его включить, нужно добавить /suggestion к концу URL.")
    web.run_app(app, host=HOST, port=PORT, print=None)