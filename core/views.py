from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm
#the view is logic that injects data from the database to the templates


def book_list(request):
    my_books = Book.objects.all()
    context = {'my_books':my_books}
    return render(request, 'core/book_list.html',context)


def book_details(request,id):
    my_book_details = Book.objects.get(book_id = id )
    return render(request, 'core/book_details.html',{'mbd' : my_book_details})

def delete_book(request,pk):
    book_obj = Book.objects.get(book_id = pk)
    if request.method == 'POST':
        book_obj.delete()
        return redirect('/shop/books')
    return render(request,'core/delete_book_confirm.html',{'book_obj':book_obj})

def create_book(request):
    print(request)
    form = BookForm(request.POST or None)#multiple ways to write code here
    if form.is_valid():
        form.save()
        return redirect('/shop/books')
    return render(request,'core/create_book.html',{'book_form':form})    

def update_book(request,id):
    book_obj = Book.objects.get(book_id = id)
    form = BookForm(request.POST or None, instance = book_obj)#multiple ways to write code here
    if form.is_valid():
        form.save()
        return redirect('/shop/books')
    return render(request,'core/create_book.html',{'book_form':form})    