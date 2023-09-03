#!/bin/bash

# Comando para activar el entorno virtual
activate_venv() {
    source venv/bin/activate
}

# Comando para instalar las dependencias
install_dependencies() {
    pip install --upgrade pip
    pip install -r requirements.txt
}

# Comando para iniciar la aplicación
start_app() {
    HOST="127.0.0.1"
    PORT="8081"
    python main.py
}

# Ejecutar los comandos
activate_venv
install_dependencies
start_app
