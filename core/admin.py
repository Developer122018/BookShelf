from django.contrib import admin
from .models import Book, Author,Cart

#admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','author','price','published_date')

admin.site.register(Author)
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user','book','quantity','total_price']
    