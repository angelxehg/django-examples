from django.db import models

class Book(models.Model):
    """
    Book Model class
    This model describes a generic book 
    """

    isbn = models.CharField(max_length=15)
    title = models.CharField(max_length=100)
    descr = models.CharField(max_length=200, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return f'Book {self.title[:20]}'
