from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Author(models.Model):
    author_name = models.CharField(max_length = 25)

    def __str__(self):
        return self.author_name

class Book(models.Model):
    book_id = models.UUIDField(default = uuid4, editable = False, primary_key = True)
    name = models.CharField(max_length = 50)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, null = True, blank = True)
    language = models.CharField(max_length = 15)
    price = models.FloatField()
    published_date = models.DateField()
    description = models.TextField(max_length= 250, blank= True, null=True)
    image = models.ImageField(upload_to = 'images/',blank = True, null = True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    book = models.ForeignKey(Book, on_delete = models.CASCADE, null = True, blank = True)
    quantity = models.IntegerField(null = True, blank = True)
    total_price = models.IntegerField(null = True, blank = True)
#  def __str__(self):
#     return self.name + '    ' + self.author + '      ' + str(self.published_date)
    # def ttprice(self):
    #     self.total_price = self.book.price * quantity
    #     return self.total_price

