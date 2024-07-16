from django.http import HttpResponse
from django.shortcuts import render
import random
from django.db.models import Q

from myapp.models import Person

def index(request):
    query=request.GET.get('query')


    if query is not None and query !="":
        # persons=Person.objects.filter(name__icontains=query)
        persons=Person.objects.filter(Q(name__startswith =query) | Q(phone__icontains=query) | Q(id__icontains=query))



    else:  
        persons=Person.objects.all().order_by('-id')


    total_person=Person.objects.all().count()
    # print(persons)
    # for person in persons:
    #     print(person.name)
    #     print(person.phone)
    #     print(person.email)
    #     print(person.address)



    data=random.randint(0,10)


    context={
        'person_list':persons,
        'total_person':total_person

    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'base.html')


person_list=[
    {
    'name':"bhijan",
    'email':"@gmail.com",
    'phone':"9812345678"
    }
]

def service(request):
    name= request.GET.get('full')
    email=request.GET.get('mail')
    phone=request.GET.get('phone')
    addres=request.GET.get('address')
    level=request.GET.get('level')
    if (name!=None and name != "") and (email !=None and email !="")and (phone !=None and phone!=""):
    
        message=f"Thank You for contacting us,your details are Name:{name},Email:{email},Phone:{phone} respectively!!"
        person_data={
            'name':name,
            'phone':phone,
            'email':email
        }
        person_list.append(person_data)

    else:
        message=""

    
    context={
        'message':message,
        'person':person_list
    }
    return render(request,'service.html',context)


def dynamic(requests):
    name="Django Site"
    email="django@email.com"
    phone="981111111"
    alternate_numbers=[
        '9812334567','981116545','98776534343'
    ]
    

    context={
        'name':name,
        'email':email,
        'phone':phone,
        'alternate_numbers':alternate_numbers,
        'display_email':False

    }
    return render(requests,'dynamic.html',context)


def add(request,a,b):
   
    return HttpResponse(f"<h1>{a+b}</h1>")
