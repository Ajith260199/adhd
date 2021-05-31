from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import contact
from .models import user_details
import pdfkit as pdf
# Create your views here.
name = ''
a = int()
def index(request):
    return render(request,'index.html')

def Home(request):
    return render(request,'Home.html')

def test(request):
    return render(request,'test.html')



def contactus(request):


    if request.method == "POST":
        Contact = contact()
        name = request.POST.get('name')
        email =request.POST.get('email')
        message = request.POST.get('message')
        Contact.name = name
        Contact.email = email
        Contact.message = message
        Contact.save()
        print(Contact.email)
        print(Contact.message)
    return render(request, 'contact-us.html')

class Uresponse:
    def __init__(self):
        self.ansList = []
        self.score = 0
    def answerdata(self,ans):
        self.ansList.append(ans)
    def getAnsData(self):
        return self.ansList
    def getScore(self):
        a = 0
        for i in self.ansList:
            a += i
        return a


def adulttest(request):
    global a
    if request.method == "POST":
        auser = Uresponse()
        for i in range(1, 8):
            auser.answerdata(int(request.POST[f'que_{i}_careless']))

        # que1 = request.POST['que_1_careless']
        # que2 = request.POST['que_2_careless']
        # que3 = request.POST['que_3_careless']
        # que4 = request.POST['que_4_careless']
        # que5 = request.POST['que_5_careless']
        # que6 = request.POST['que_6_careless']
        # que7 = request.POST['que_7_careless']

        # totalque1 = int(que1)
        # totalque2 = int(que2)
        # totalque3 = int(que3)
        # totalque4 = int(que4)
        # totalque5 = int(que5)
        # totalque6 = int(que6)
        # totalque7 = int(que7)
        # a = totalque1+totalque2+totalque7+totalque6+totalque5+totalque3+totalque4
        print(auser.getScore())
        adhddetails = user_details()
        adhddetails.name = name
        adhddetails.score = auser.getScore()
        if a >= 0 and a <= 10:
            return render(request, 'no adhd.html', {'adhddetails': adhddetails})
        elif a > 10 and a <= 15:
            return render(request, 'mild adhd.html', {'adhddetails': adhddetails})
        elif a > 15 and a <= 42:
            return render(request,'severe adhd.html',{'adhddetails':adhddetails})
    else:
        return render(request,'adult-test.html')



def adultdetails(request):

    if request.method == "POST":
        global name
        name = request.POST['username']
        email = request.POST['email']
        print(name)
        print(email)
        return render(request, 'adult-test.html')



def childtest(request):
    return render(request,'child-test.html')