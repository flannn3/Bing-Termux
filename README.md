<h1 align="center">Biba</h1>

## ¿Qué es esto?
Conexión del bot GPT-4 Sidney desde Bing a la Taberna

## ¿Qué se puede hacer?
Confuso.</br>
14-20k tokens.</br>
Codificación en un flujo de trabajo funcional (mejor que Scala).</br>
Extracción de datos de Internet.</br></br>
![imagen](https://github.com/Barbariskaa/Biba/assets/129290831/b5176621-4a1f-4b57-9c7f-865861825c30)</br></br>
Obtención de sugerencias de Bing (a través de /suggestion después del modo especificado en la URL).</br></br>
![imagen](https://user-images.githubusercontent.com/129290831/236729981-42f4cbf8-abbd-4deb-9a70-1a1cb5917119.png)

## ¿Y respecto a los problemas?
Las respuestas del servidor se filtran en medio del flujo, como en un té. En promedio, se eliminan alrededor de 100 tokens y hasta varios cientos. Depende del modo seleccionado.<br>
Es posible que este límite se pueda evitar si se trabaja con los prompts.</br>
Las respuestas detenidas se unen en una sola.</br>
También hay bloqueos. Pueden banear en un día o tal vez no. Se resuelve recargando.</br>
A partir del 29 de mayo de 2023, puede haber problemas de funcionamiento desde IPs rusas si se utiliza el script sin VPN.

## Cómo instalar en Termux
Para instalar Biba en Termux, sigue estos pasos:

1. Abre Termux en tu dispositivo.

2. Clona el repositorio Biba ejecutando el siguiente comando:

   ```shell
   git clone https://github.com/Barbariskaa/Biba.git
   ```
Esto descargará el código fuente de Biba en tu directorio actual.

1. Navega al directorio "Biba" utilizando el comando "cd". Ejecuta el siguiente comando para hacerlo:
    ```shell
    cd Biba
     ```
    
2. Una vez que estés en el directorio "Biba", ejecuta el archivo "start.sh" con el siguiente comando:
     ```shell
    sh start.sh
     ```
