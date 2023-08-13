from django.shortcuts import render, redirect
from .forms import YourTaskForms
from .models import YourTask

def ShowTask(request):
    datas=YourTask.objects.all()
    print(datas)
    return render(request,'show_task.html',{'data': datas})


def AddTask(request):
    if request.method == 'POST':
        datas = YourTaskForms(request.POST)
        if datas.is_valid():
            print(datas.cleaned_data)
            datas.save()
            return redirect('showtask')
    else:
        datas = YourTaskForms()
        
    return render(request, 'add_task.html', {'data': datas})

              
def DeleteTask(rquest,id):
    task=YourTask.objects.get(pk = id).delete()
    return redirect('showtask')
   
   
def EditTask(request, id):
    task = YourTask.objects.get(pk = id)
    form = YourTaskForms(instance = task)
    if request.method == 'POST':
        form = YourTaskForms(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('showtask')
    return render(request, 'edit_task.html', {'form':form})
                    
    


def complete_task(request, id):
    task = YourTask.objects.get(id=id)
    task.is_completed = 1   
    task.save()
    completed_tasks = YourTask.objects.filter(is_completed=1)
    return render(request, 'completed_task.html', {'completed_tasks': completed_tasks})


def CompletedPage(request):
    completed_tasks = YourTask.objects.filter(is_completed=1)
    return render(request,'completed_task.html',{'completed_tasks': completed_tasks})
    
def ShowTaskPage(request):
    datas=YourTask.objects.all()
    print(datas)
    return render(request,'show_task.html',{'data': datas})

