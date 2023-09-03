<h1 align="center">Bing-Termux</h1>

## ¿Qué es esto?
La Conexión del bot GPT-4 Sidney desde Bing a Tavern o SillyTavern desde Termux.

## ¿Como Obtener la cookies?
Requisitos:

Una computadora con Microsoft Edge instalado.
Inicia sesión con la cuenta de la que deseas extraer las cookies.
Pasos:

1. Instala la Extensión "Cookie Edit":

Abre Microsoft Edge en tu computadora.
En el navegador, busca "Cookie Edit" y procede a instalar esta extensión.
Inicia una Conversación con Bing:

2. Ve a la página principal del navegador.
Interactúa con la extensión seleccionando el ícono que se asemeja a una conversación con Bing. Mantén una conversación mínima de al menos dos mensajes.

3. Exporta las Cookies:

Después de interactuar, busca el ícono de  extensión y haz clic en él.
A continuación, selecciona la opción para exportar las cookies en un archivo JSON.

Lo tendras copiado, y solo lo tienes que pegar en el archivo Cookie.json que esta en este repositorio o crear uno en block de notas pegarlo y nombrarlo cookie.json.

## ¿Tiene algun limite?
Sí, existe un límite diario, pero no es excesivo.

## Baneos
El ban, un miedo de algunas personas, "es raro que te baneen ya que desde las misma documentación establece literalmente que el modelo no está diseñado para seguir estrictamente las reglas que se le indican en sus indicaciones,by u/Successful_Cap_390", Asi que los jailbreak no son un problemas, a menos que lo uses para cosas ilegales como fabricacion de codigos maliciosos o como crear cosas ilegales, te recuerdo que bing usa tu ip al navegar por internet.

## Instalacion en Termux
Para instalar en Termux, sigue estos pasos:

1. Abre Termux en tu dispositivo y pon:

      ```shell
     pkg install git
      ```

2. Clona el repositorio este ejecutando el siguiente comando:

      ```shell
     git clone https://github.com/flannn3/Bing-Termux
      ```

Esto descargará el código fuente de Biba en tu directorio actual.

3. Navega al directorio "Biba" utilizando el comando "cd". Ejecuta el siguiente comando para hacerlo:

     ```shell
    cd Bing-Termux
     ```
    
4. Una vez que estés en el directorio "bing", ejecuta el archivo "instalacion.sh" con el siguiente comando:

     ```shell
    sh instalacion.sh
     ```

     Esto lo instala e inicia.
   
5. Si quieres volver a iniciarlo  solo tienes que abrir el directorio con:

     ```shell
    cd Bing-Termux
     ```
   Y ejecutar con este ultimo:

     ```shell
    sh instalacion.sh
     ```
   Sera mas rapido al ya estar instalado.
     
## Captcha
Si te encuentras con problemas como el Captcha, la solución es relativamente sencilla. Sigue estos pasos para resolverlo:

1. Ve a la aplicación de Bing en tu navegador web y accede con la misma cuenta desde la cual obtuviste la cookie.

2. Inicia una conversación con Bing enviando al menos 2 mensajes. Esto debería ser suficiente para solucionar el problema del Captcha.

Recuerda que es importante que utilices la misma cuenta desde la cual obtuviste la cookie para garantizar una solución exitosa.


##  Creditos
Este trabajo solo fue con el proposito de facilitar la ejecucion para Termux Todo trabajo y credito se lo lleva:
https://github.com/Barbariskaa/Biba
El Github original
