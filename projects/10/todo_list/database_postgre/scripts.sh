sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt-get install -y postgresql postgresql-contrib
sudo systemctl status postgresql

sudo passwd postgres

sudo -i -u postgres
psql postgres
\l
\d
CREATE USER todolist_usr WITH PASSWORD '12345Qwerty!';
CREATE DATABASE todolist_db OWNER todolist_usr;

\q
psql todolist_db

create table todos (id serial not null unique, title varchar(255) not null unique, description varchar(1024), date_create timestamp not null default now(), status bool default 'false');

\d

GRANT ALL PRIVILEGES ON DATABASE todolist_db TO todolist_usr;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to todolist_usr;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to todolist_usr;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public to todolist_usr;

select * from todos;
insert into todos (title, description, status) values ('Купить кота', 'Купить Купить Купить', 'true');
select * from todos;



