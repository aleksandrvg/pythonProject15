from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
class MyClass:
    string = ""
    def __init__(self, s):
        self.string = s
def main(request):
    my_num = 33
    my_str = "my string"
    my_dict = {"some_key": "some_value"}
    my_list = ["list_first_item", "list_second_item", "list_third_item"]
    my_class = MyClass('class string')
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_class': my_class,
        'display_num': False,
        'now': datetime.datetime.now()
    })
def usname(request):
    username = "Abra kadara"
    return render(request, "usname.html", {"usname": username})
def first(request):
    return HttpResponse("Переход по ссылке")
def two(request, one, two):
    return HttpResponse(f"My two response {one * two}")

def test(request):
    return HttpResponse("Two but another")