sudo docker-compose ps
sudo docker-compose build
sudo docker-compose up
sudo docker-compose up -d
sudo docker-compose down

docker-compose run app sh -c "django-admin startproject django_settings ."

redis-cli -h 127.0.0.1 -p 6380

sudo docker-compose up -d --build

    depends_on:
      - db
  db:
    image: postgres:13-alpine
    environment:
      - POSTGRES_DB=app
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=supersecretpassword
    ports:
      - "5432:5432"