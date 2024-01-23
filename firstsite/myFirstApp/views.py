from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
import datetime
# Create your views here.
class MyClass:
    string = ""
    def __init__(self, s):
        self.string = s

def main(request):
    return render(request, 'index.html')
def my_login(request):
    from django.contrib.auth import login
    if request.method == 'POST':
        form = AuthentificationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect('/')
    else:
        form = AuthentificationForm()
    return render(request, 'login.html', {'form': form})
from django.contrib.auth.decorators import login_required
@login_required(login_url='accaunt/login/')
def logout_user(request):
    from django.contrib.auth import logout
    if request.method == 'POST':
        if request.user.is_authenticated:
            pass
    logout(request)
def form_view(request):
    # return render(request, 'form.html')
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            return render(request, 'formValid.html')
    else:
        form = MyForm()
    return render(request, "form.html", {'form': form})
    # my_num = 33
    # my_str = "my string"
    # my_dict = {"some_key": "some_value"}
    # my_list = ["list_first_item", "list_second_item", "list_third_item"]
    # my_class = MyClass('class string')
    # return render(request, 'index.html', {
    #     'my_num': my_num,
    #     'my_str': my_str,
    #     'my_dict': my_dict,
    #     'my_list': my_list,
    #     'my_class': my_class,
    #     'display_num': False,
    #     'now': datetime.datetime.now()
    # })
def usname(request):
    username = "Abra kadara"
    return render(request, "usname.html", {"usname": username})
def first(request):
    return HttpResponse("Переход по ссылке")
def two(request, one, two):
    return HttpResponse(f"My two response {one * two}")

def test(request):
    return HttpResponse("Two but another")


def fun():
    try:
        return Comment.objects.get(article_genre_in=[2,3])
    except Comment.MultipleObjectReturned:
        return "More then one object"
    except Comment.DoesNotExist:
        return "Cant find object"
def fun2():
    Comment.objects.all()
    Comment.objects.filter(text="Hey everyone")