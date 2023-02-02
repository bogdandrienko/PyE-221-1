@echo OFF

cd ..\



python.exe -m pip install --upgrade pip

pip install env

python -m venv env

call .\env\Scripts\activate.bat

python.exe -m pip install --upgrade pip



cmd