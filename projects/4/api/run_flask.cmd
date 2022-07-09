cd ..

call env/Scripts/activate.bat

set FLASK_APP=api/main
flask run --host=0.0.0.0

cmd
