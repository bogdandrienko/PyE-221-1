@echo OFF

cd ..\

@REM rmdir /Q /S static

@REM mkdir static

call .\env\Scripts\activate.bat



python manage.py collectstatic --noinput

@REM rmdir /Q /S react\production\static

@REM rmdir /Q /S react\test\static

call cmd