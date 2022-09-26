@echo OFF

pip install --upgrade pip

pip install env

set /p project_variable= "Please set your project name: "

IF "%project_variable%"=="" (set project_variable="project_folder")

mkdir %project_variable% && cd %project_variable%

set /p env_variable= "Please set your virtual environment name: "

IF "%env_variable%"=="" (set env_variable="env")

python -m venv %env_variable%

call %env_variable%/Scripts/activate.bat

cmd