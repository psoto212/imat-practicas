#!/bin/sh

echo "Despliegue del proyecto FUSO"

PROJECT_DIR="ProyectoFUSO"

echo "Clonando repositorio"
if [ -d "$PROJECT_DIR" ]; then
    rm -rf "$PROJECT_DIR"
fi
git clone https://github.com/pablosanchezp/ProyectoFUSO.git

echo "Creando entorno virtual"
python3 -m venv "$PROJECT_DIR/venv"

echo "Activando entorno virtual"
. "$PROJECT_DIR/venv/bin/activate"

echo "Instalando dependencias"
pip install -r "requirements.txt"

echo "Ejecutando aplicación"
python3 "$PROJECT_DIR/main.py"
