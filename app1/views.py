from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return render(request, "jquery_ajax_add_nums.html")


def add(request):
    if request.method == "POST":
        num1 = request.POST.get("num1", 0)
        num2 = request.POST.get("num2", 0)
        result = int(num1) + int(num2)
        return JsonResponse({"result": result})    