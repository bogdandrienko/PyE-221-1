from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-publication_date', 'title']

    def __str__(self):
        return f"({self.id}) {self.title}"

