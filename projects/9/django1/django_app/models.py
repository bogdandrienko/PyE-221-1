from django.db import models

# --CREATE USER django_user WITH PASSWORD '12345Qwerty!';

# --alter user django_user with password '12345Qwerty!';

# --CREATE DATABASE django_database OWNER django_user;

# --GRANT ALL PRIVILEGES ON DATABASE django_database TO django_user;

# Create your models here.
class Product(models.Model):
    label = models.CharField("Наименование", max_length=100, unique=True)
    amount = models.IntegerField("Количество")
    not_bubble_price = models.IntegerField("Стоимость без накрутки")
    bubble_percentage = models.IntegerField("Процент накрутки")
    final_price = models.IntegerField("Итоговая стоимость")
    vat_price = models.IntegerField("Стоимость с НДС")
    overall = models.IntegerField("Итоговая")

    def __repr__(self):
        return str(self.label)

    def __str__(self):
        return str(self.label)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
