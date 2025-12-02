# Script de inicialización para PPS_Unidad1 (Windows)
# Autor: Alejandro Rodriguez

$project = "."  # Carpeta actual

# 1. Crear directorios base
New-Item -Path "$project/src/modulo1" -ItemType Directory -Force
New-Item -Path "$project/src/modulo2" -ItemType Directory -Force
New-Item -Path "$project/tests" -ItemType Directory -Force

# 2. Crear __init__.py para los paquetes
New-Item -Path "$project/src/__init__.py" -ItemType File -Force
New-Item -Path "$project/src/modulo1/__init__.py" -ItemType File -Force
New-Item -Path "$project/src/modulo2/__init__.py" -ItemType File -Force
New-Item -Path "$project/tests/__init__.py" -ItemType File -Force

# 3. Crear archivos vacíos
New-Item -Path "$project/src/modulo1/funciones.py" -ItemType File -Force
New-Item -Path "$project/src/modulo2/clases.py" -ItemType File -Force
New-Item -Path "$project/src/binario.py" -ItemType File -Force
New-Item -Path "$project/src/lista.py" -ItemType File -Force
New-Item -Path "$project/src/main.py" -ItemType File -Force
New-Item -Path "$project/tests/test_modulo1.py" -ItemType File -Force
New-Item -Path "$project/tests/test_pytest.py" -ItemType File -Force
New-Item -Path "$project/.gitignore" -ItemType File -Force
New-Item -Path "$project/requirements.txt" -ItemType File -Force
New-Item -Path "$project/README.md" -ItemType File -Force

Write-Host "Estructura generada. Ya puedes rellenar los archivos."