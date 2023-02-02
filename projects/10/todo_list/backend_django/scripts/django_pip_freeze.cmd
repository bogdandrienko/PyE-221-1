@echo OFF

cd ..\

call .\env\Scripts\activate.bat



pip freeze > requirements.txt



call cmd