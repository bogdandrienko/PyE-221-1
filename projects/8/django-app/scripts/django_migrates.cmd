@echo OFF

cd ..\

call .\env\Scripts\activate.bat



python manage.py makemigrations

python manage.py migrate



call cmd