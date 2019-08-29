from django.db import models
from uuid import uuid4

class Book(models.Model):
    book_id = models.UUIDField(default = uuid4, editable = False, primary_key = True)
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 25)
    language = models.CharField(max_length = 15)
    price = models.FloatField()
    published_date = models.DateField()
    description = models.TextField(max_length= 250, blank= True, null=True)

#  def __str__(self):
#     return self.name + '    ' + self.author + '      ' + str(self.published_date)
    

