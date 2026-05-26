from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Todolist

def list(request):
    lists=Todolist.objects.all()
    return render(request,'home.html',{'lists':lists})

def add(request):
    if request.method =='POST':
        task=request.POST.get('task')

        if not task:
             messages.error(request,"tasks are required")
             return redirect('add')
        
        Todolist.objects.create(
            task=task
        )

        messages.success(request,"task added successfully")
        return redirect(list)
    
    return render(request,'add.html')

def update(request,id):
    lists=get_object_or_404(Todolist,id=id)
    if request.method=='POST':
        lists.task=request.POST.get('task')

        lists.save()

        messages.success(request,'task added successfully')
        return redirect('list')
    
    return render(request,'update.html',{'lists':lists})

def delete(request,id):
    lists=get_object_or_404(Todolist,id=id)
    if request.method =="POST":

        lists.delete()

        messages.success(request,"task deleted successfully")
        return redirect('list')
    return render(request,'delete.html',{'lists':lists})




