from django.shortcuts import render
from .models import contact, applyhere
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "base.html")

def success(request):
    return render(request, "success.html")

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        person = contact(name=name, mobile=mobile, email=email, subject=subject, message=message)
        person.save()
        return render(request, "success.html")
    return render(request, "index.html")

def form(request):
    return render(request, "form.html")


def former(request):
    if request.method == 'POST':
        emailid = request.POST.get('emailid')
        profile = request.POST.get('profile')
        linkedin = request.POST.get('linkedin')
        ceo = request.POST.get('ceo')
        startup = request.POST.get('startup')
        weblink = request.POST.get('weblink')
        estdate = request.POST.get('estdate')
        targetmarket = request.POST.get('targetmarket')
        targetsize = request.POST.get('targetsize')
        funding = request.POST.get('funding')
        investors = request.POST.get('investors')
        monthrevenue1 = request.POST.get('monthrevenue1')
        monthrevenue2 = request.POST.get('monthrevenue2')
        monthrevenue3 = request.POST.get('monthrevenue3')
        presentation = request.POST.get('presentation')
        person = applyhere(emailid=emailid, profile=profile, linkedin=linkedin, ceo=ceo, startup=startup, weblink=weblink, 
            estdate=estdate, targetmarket=targetmarket, targetsize=targetsize, funding=funding, investors=investors, 
            monthrevenue1=monthrevenue1, monthrevenue2=monthrevenue2, monthrevenue3=monthrevenue3, presentation=presentation)
        person.save()
        return render(request, "base.html")
    return render(request, "index.html")