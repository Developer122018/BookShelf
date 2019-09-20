from django.contrib import admin
from .models import Book, Author

#admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','author','price','published_date')

admin.site.register(Author)