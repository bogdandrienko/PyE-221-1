from django.db import models


# Create your models here.

class Book(models.Model):
    # id = autofield() - AUTOINCREMENT / SERIAL (POSTGRESQL)
    title = models.CharField(max_length=254)

    def __str__(self):
        return f"Book {self.title} ({self.id})"
