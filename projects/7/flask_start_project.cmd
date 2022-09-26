mkdir flask_app
cd flask_app
python -m venv env
call env/Scripts/activate.bat
pip install --upgrade pip
pip install flask
cd ..
copy main.py flask_app
cd flask_app
flask --app main run