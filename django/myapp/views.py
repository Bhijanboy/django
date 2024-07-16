from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person

# Create your views here.

def create_person(request):
   
    form=PersonForm()
    if request.method=="POST":
        form=PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context={
        'form':form

    }
    return render(request,'myapp/create_person.html',context)

def edit_person(request,id):
    #get the user form the database using id
    #fill the data in the form and render the form
    person=Person.objects.get(id=id)
    form=PersonForm(instance=person)

   

    if request.method=="POST":
        form=PersonForm(request.POST,instance=person)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={
        'form':form

    }
        
    return render(request,'myapp/edit_person.html',context)

def delete_person(request,id):
    person=Person.objects.get(id=id)
    if request.method=="POST" :
        person.delete()
        return redirect('/')

    context={
        'person':person
    }

    return render(request,'myapp/delete_person.html',context)




   
