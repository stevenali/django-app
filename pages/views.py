from django.shortcuts import redirect, render
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Contact
from django.views.decorators.csrf import csrf_exempt
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
@csrf_exempt
def contactbackend(request):
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        Contact.objects.create(name=name, email=email, message = message)
        return JsonResponse({"sa":"as"})
    else:
        return redirect("/")
def error404(request,exception):
    return render(request,'404.html' ,status=404)
def error500(request):
    return render(request,'404.html' ,status=500)