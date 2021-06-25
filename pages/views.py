from django.shortcuts import redirect, render
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage , send_mail
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
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
        email_subject1 = "merhaba "+name
        email_body1 = f"{email}     -     {message}"
        html_content =  f"<h1>{message}</h1><h4>{email}     -     {message}</h4>"
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives("subject", text_content, 'noreply.aliwkochannels@gmail.com', ["alicankilic1905@hotmail.com"])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        
        email2 = EmailMessage(
            email_subject1 ,
            email_body1,
            'noreply.aliwkochannels@gmail.com',
            ["alicankilic1905@hotmail.com"],
        )
        email2.send(fail_silently = False)
        return JsonResponse({"sa":"as"})
    else:
        return redirect("/")
def error404(request,exception):
    return render(request,'404.html' ,status=404)
def error500(request):
    return render(request,'404.html' ,status=500)