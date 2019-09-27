from django.urls import path
from django.views.generic import RedirectView
#from .views import home
from . import views #whole file imports
#from views import home

urlpatterns=[
    path('books/',views.book_list),
    path('',RedirectView.as_view(url = 'books')),
    path('details/<uuid:id>/',views.book_details,name = 'detail_book'),
    path('delete/<uuid:pk>/',views.delete_book),
    path('book/create/',views.create_book),
    path('update/<uuid:id>/',views.update_book)
]