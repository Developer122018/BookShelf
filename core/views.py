from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required 
#the view is logic that injects data from the database to the templates

#this function displays the basic data of the books on the homepage

def book_list(request):
    my_books = Book.objects.all()
    context = {'my_books':my_books}
    return render(request, 'core/book_list.html',context)

#this provides details for each book with the price, author etc
@login_required()
def book_details(request,id):
    my_book_details = Book.objects.get(book_id = id )
    return render(request, 'core/book_details.html',{'mbd' : my_book_details})

#gets the books id and deletes after a confirmation
@login_required()
def delete_book(request,pk):
    book_obj = Book.objects.get(book_id = pk)
    if request.method == 'POST':
        book_obj.delete()
        return redirect('/shop/books')
    return render(request,'core/delete_book_confirm.html',{'book_obj':book_obj})

#creates a new book and adds it to the database
@login_required()
def create_book(request):
    form = BookForm(request.POST or None, request.FILES)#multiple ways to write code here
    print(form)
    if form.is_valid():
        authors_name = request.POST.get('author')
        print(authors_name)                                                                                                                                    
        form.save()
        return redirect('/shop/books')
    return render(request,'core/create_book_2.html',{'book_form':form})    

#updates an existing book and uses forms to do so
@login_required()
def update_book(request,id):
    book_obj = Book.objects.get(book_id = id)
    form = BookForm(request.POST or None, instance = book_obj)#multiple ways to write code here
    if form.is_valid():
        form.save()
        return redirect('/shop/books')
    return render(request,'core/create_book.html',{'book_form':form})    

