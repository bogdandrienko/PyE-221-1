#! bash

# update os
sudo apt update -y
sudo apt-get update -y
sudo apt upgrade -y
sudo apt-get upgrade -y
# clear cache
sudo apt autoremove -y
##################################

# clear terminal
clear
#######################

# vbox
!vbox insert guest-additions
sudo apt install -y build-essential dkms linux-headers-$(uname -r)
sudo apt-get install build-essential linux-headers-`uname -r` dkms virtualbox-dkms
sudo mkdir -p /mnt/cdrom
sudo mount /dev/cdrom /mnt/cdrom
cd /mnt/cdrom
sudo sh ./VBoxLinuxAdditions.run --nox11
sudo adduser user vboxsf
sudo reboot
#################################

# установка удалённого доступа по ssh
sudo apt install -y openssh-server
sudo systemctl start ssh
sudo systemctl restart ssh
###############################

# зависимости для линукса
sudo apt install -y build-essential libpq-dev unixodbc-dev zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev
# вспомогательные пакеты и модули
sudo apt install -y curl wget git htop net-tools docker-compose virtualbox virtualbox-ext-pack
# основные веб модули
sudo apt install -y nginx gunicorn python3-dev python3-pip python3-venv postgresql postgresql-contrib mysql-server
systemctl start mysql.service
# автоматическая выдача SSL сертификатов
sudo snap install --classic certbot
# github CLI
sudo snap install gh
# стандартная группа для nginx
sudo usermod -aG user www-data
#################################################################

# удаление файла
sudo rm temp.txt
# редактирование / создание файла
nano new.json



#####################################################################
# POSTGRESQL
sudo apt update -y
sudo apt install -y postgresql postgresql-contrib
sudo passwd postgres
sudo -i -u postgres
#sudo su - postgres
createuser django_user
createdb django_database -O django_user
psql django_database
CREATE USER django_user WITH PASSWORD '12345Qwerty!';
alter user django_user with password '12345Qwerty!';

CREATE DATABASE django_database OWNER django_user;
GRANT ALL PRIVILEGES ON DATABASE django_database TO django_user;

\q
exit

sudo nano /etc/postgresql/14/main/postgresql.conf
# listen_addresses = '*'
sudo nano /etc/postgresql/14/main/pg_hba.conf
# host    all             all             192.168.0.165/32         scram-sha-256
# host    all             all             all         scram-sha-256

sudo systemctl stop postgresql
sudo systemctl status postgresql
sudo systemctl restart postgresql
sudo systemctl status postgresql


sudo -i -u postgres
psql
\connect django_database


CREATE TABLE zarplata ( id serial PRIMARY KEY, username VARCHAR ( 50 ) UNIQUE NOT NULL, salary INT );
select * from zarplata;

insert into zarplata (username, salary) VALUES ('Bogdan', '60000'), ('Alice', '80000');
select * from zarplata;

delete from zarplata where username = 'Bogdan';
select * from zarplata;

###########################################################


#############################################################
# DJANGO

python3 -m pip3 install --upgrade pip
python3 -m venv env

source env/bin/activate
python3 -m pip3 install --upgrade pip

pip install wheel
pip install Django djangorestframework django-cors-headers django-environ django-grappelli djangorestframework-simplejwt gunicorn celery redis psycopg2-binary pyodbc lxml Pillow requests aiohttp beautifulsoup4 openpyxl
pip install -r requirements.txt
pip freeze > requirements.txt

django-admin startproject django_settings .
django-admin startapp django_app

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username admin --email bogdandrienko@gmail.com

python manage.py collectstatic --noinput
python manage.py createcachetable
python manage.py check --database default

python manage.py runserver 0.0.0.0:8000
gunicorn --bind 0.0.0.0:8000 django_settings.wsgi

####################################################################


#############################################################
# gunicorn

sudo nano /etc/systemd/system/gunicorn.socket
<file>
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
</file>

sudo nano /etc/systemd/system/gunicorn.service
<file>
[Unit]
Description=Gunicorn for the Django example project
Requires=gunicorn.socket
After=network.target

[Service]
Type=notify

User=user
Group=www-data

RuntimeDirectory=gunicorn
WorkingDirectory=/home/user/Downloads/web2
ExecStart=/home/user/Downloads/web2/env/bin/gunicorn --workers 9 --bind unix:/run/gunicorn.sock django_settings.wsgi:application
ExecReload=/bin/kill -s HUP $MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-user.target
</file>

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable --now gunicorn.service
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl status gunicorn.service
#sudo systemctl disable gunicorn
#sudo systemctl stop gunicorn

####################################################################

#############################################################
# nginx

sudo nano /etc/nginx/sites-available/192.168.0.116-http.conf
<file>
server {
listen 80;
listen [::]:80;

server_name 192.168.0.116;

root /home/user/Download/web2;

location /.well-known/acme-challenge/ {}

location /favicon.ico {
    alias /home/user/Download/web2/static/logo.png;

    access_log off; log_not_found off;

    expires max;
}

location /robots.txt {
    alias /home/user/Download/web2/static/robots.txt;

    access_log off; log_not_found off;

    expires max;
}

location /static/ {
    alias /home/user/Download/web2/static/;

    expires max;
}

location /media/ {
    alias /home/user/Download/web2/static/media/;

    expires max;
}

location / {
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header Host $http_host;
    proxy_redirect off;
    proxy_buffering off;
    proxy_pass http://unix:/run/gunicorn.sock;
}
}
</file>

sudo ln -s /etc/nginx/sites-available/192.168.0.116-http.conf /etc/nginx/sites-enabled/192.168.0.116-http.conf
sudo nginx -t
sudo service nginx start
sudo systemctl status nginx.service
sudo ufw allow 'Nginx Full'
sudo systemctl reload nginx.service
####################################################################