python -m venv env
call env/scripts/activate
python -m pip install --upgrade pip
pip install django pillow 
django-admin startproject app_config .
django-admin startapp posts

cmd