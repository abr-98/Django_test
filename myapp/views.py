from django.shortcuts import render
import datetime
from myapp.models import Dreamreal
# Create your views here.
from django.http import HttpResponse

#from django.http import HttpResponse

def hello(request):
    today = datetime.datetime.now().date()
    return render(request, "hello.html", {"today" : today})

def morning(request):
    today = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    return render(request, "morning.html", {"today" : today,"time" : time})

def days(request):
    today = datetime.datetime.now().date()
    
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "days.html", {"today" : today, "days_of_week" : daysOfWeek})

def main_h(request):
    today = datetime.datetime.now().date()
    
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "hello_2.html", {"today" : today, "days_of_week" : daysOfWeek})

def crudops(request):
    dreamreal=Dreamreal(
        website="www.github.com",mail="abhijitroy1998@gmail.com",
        name='Abhijit',phonenumber="8900453085"
    )

    dreamreal.save()

    objects=Dreamreal.objects.all()
    res ='Printing all Dreamreal entries in the DB : <br>'

    for elt in objects:
        res += elt.name+"<br>"

    sorex = Dreamreal.objects.get(name = "Abhijit")
    res += 'Printing One entry <br>'
    res += sorex.name
   
    #Delete an entry
    res += '<br> Deleting an entry <br>'
    sorex.delete()
    #Update
    dreamreal = Dreamreal(
    website = "www.polo.com", mail = "sorex@polo.com", 
    name = "sorex", phonenumber = "002376970"
    )
    dreamreal.save()
    dreamreal = Dreamreal(
    website = "www.polo.com", mail = "paul@polo.com", 
    name = "paul", phonenumber = "002638330"
    )
    dreamreal.save()
    res += 'Updating entry<br>'
    
    dreamreal = Dreamreal.objects.get(name = 'sorex')
    dreamreal.name = 'thierry'
    dreamreal.save()
    
    return HttpResponse(res)

def datamanipulation(request):
    res = ''
    
    #Filtering data:
    qs = Dreamreal.objects.filter(name = "paul")
    res += "Found : %s results<br>"%len(qs)
    
    #Ordering results
    qs = Dreamreal.objects.order_by("name")
    
    for elt in qs:
        res += elt.name + '<br>'
    
    return HttpResponse(res)


def viewArticle(request, articleId):
    """ A view that display an article based on his ID"""
    text = "Displaying article Number : %s" %articleId
    return HttpResponse(text)
         
def viewArticles(request, year, month):
    text = "Displaying articles of : %s/%s"%(year, month)
    return HttpResponse(text)


    ''' REDIRECTION EXAMPLES'''
from django.shortcuts import redirect

def hello_3(request):
    today = datetime.datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return redirect("https://www.djangoproject.com")

def viewArticle_2(request, articleId):
    """ A view that display an article based on his ID"""
    text = "Displaying article Number : %s" %articleId
    return redirect(viewArticles_2, year = "2045", month = "02")
     
def viewArticles_2(request, year, month):
    text = "Displaying articles of : %s/%s"%(year, month)
    return HttpResponse(text)
 

'''Sending emails'''

'''To start sending e-mail, edit your project settings.py file and set the following options −

EMAIL_HOST − smtp server.

EMAIL_HOST_USER − Login credential for the smtp server.

EMAIL_HOST_PASSWORD − Password credential for the smtp server.

EMAIL_PORT − smtp server port.

EMAIL_USE_TLS or _SSL − True if secure connection.

'''

from django.core.mail import send_mail
#from django.http import HttpResponse

def sendSimpleEmail(request,emailto):
   res = send_mail("hello paul", "comment tu vas?", "paul@polo.com", [emailto])
   return HttpResponse('%s'%res)

'''
Here is the details of the parameters of send_mail −

subject − E-mail subject.

message − E-mail body.

from_email − E-mail from.

recipient_list − List of receivers’ e-mail address.

fail_silently − Bool, if false send_mail will raise an exception in case of error.

auth_user − User login if not set in settings.py.

auth_password − User password if not set in settings.py.

connection − E-mail backend.

html_message − (new in Django 1.7) if present, the e-mail will be multipart/alternative.

'''

