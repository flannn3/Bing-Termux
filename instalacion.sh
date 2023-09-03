#!/bin/bash
pkg update
pkg upgrade
pkg install python
pkg pip
pkg install python-pip
pkg install python3-venv
pkg install rust
pip install tiktoken
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
