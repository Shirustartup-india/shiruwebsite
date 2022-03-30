from django.shortcuts import render
from .models import contact, applyhere
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
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
		messages.success(request, 'Request Sent Successfully')
		subject = "Enquiry"
		body = {
			'name' : str("Name :" + request.POST.get('name')),
		'mobile' : str("Phone No.: " + request.POST.get('mobile')),
		'email' : str("Email id: " + request.POST.get('email')),
		'subject' : str("Subject: " + request.POST.get('subject')),
		'message' : str("Message :" + request.POST.get('message')),
		}
		message = "\n".join(body.values())
		try:
			send_mail(subject, message, 'shirustartup.cafe@gmail.com', ['shirustartup.cafe@gmail.com']) 
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		return render(request, "base.html")
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
		messages.success(request, 'Registration Details Sent Successfully')
		subject = "New Entry"
		body = {
			'emailid' : str("Email: " + request.POST.get('emailid')),
			'profile' : str("Founder Profile: " + request.POST.get('profile')),
		'linkedin' : str("LinkedIn Profile: " + request.POST.get('linkedin')),
		'ceo' : str("CEO: " + request.POST.get('ceo')),
		'startup' : str("Startup-name: " + request.POST.get('startup')),
		'weblink' : str("Website-link: " + request.POST.get('weblink')),
		'estdate' : str("Establishment Date: " + request.POST.get('estdate')),
		'targetmarket' : str("Target Market: " + request.POST.get('targetmarket')),
		'targetsize' : str("Target Market Size: " + request.POST.get('targetsize')),
		'funding' : str("Funding: " + request.POST.get('funding')),
		'investors' : str("Investors: " + request.POST.get('investors')),
		'monthrevenue1' : str("Last month revenue: " + request.POST.get('monthrevenue1')),
		'monthrevenue2' : str("Second last month revenue: " + request.POST.get('monthrevenue2')),
		'monthrevenue3' : str("Third last month revenue: " + request.POST.get('monthrevenue3')),
		'presentation' : str("Presentation Link: " + request.POST.get('presentation'))
		}
		message = "\n".join(body.values())
		try:
			send_mail(subject, message, 'shirustartup.cafe@gmail.com', ['shirustartup.cafe@gmail.com']) 
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		return render(request, "base.html")
	return render(request, "index.html")