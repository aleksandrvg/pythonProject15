from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main(request):
    return HttpResponse("My first response")

def two(request, one, two):
    return HttpResponse(f"My two response {one * two}")

def test(request):
    return HttpResponse("Two but another")