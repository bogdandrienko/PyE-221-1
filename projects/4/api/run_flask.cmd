cd ..

call env/Scripts/activate.bat

set FLASK_APP=api/main

set FLASK_ENV=development

flask run --host=0.0.0.0

cmd
