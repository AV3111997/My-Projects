from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . models import Task, CompletedTask
from . forms import TaskForm
from django.views.generic import ListView, DetailView, UpdateView, DeleteView



# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = "index.html"
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = "details.html"
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = "update.html"
    context_object_name = 'task'
    fields = ('task', 'priority', 'date')
    def get_success_url(self):
        return reverse_lazy('cbv_details', kwargs={'pk': self.object.pk})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "delete.html"
    success_url = reverse_lazy('cbv_home')

def index(request):
    context={}
    tasks = Task.objects.all()
    complete_task = CompletedTask.objects.all()
    context['tasks']=tasks
    context['completed_task']=complete_task
    return render(request, 'index.html',context)

def add_task(request):
    if request.method=='POST':
        task=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        addtask=Task(task=task,priority=priority,date=date)
        addtask.save()
    return redirect("/")

def delete_task(request, id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect("/")

def complete_task(request, id):
    task = Task.objects.get(id=id)
    task_name = task.task
    date = task.date
    task_complete = CompletedTask(completed_task=task_name, completed_date=date)
    task_complete.save()
    task.delete()
    return redirect("/")

def update_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm(instance=task)
        context = {
        'form': form,
        'task': task,
        }
    return render(request, 'update.html', context)

def delete_task(request, id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect("/")

def completed_task_clear(request):
    task=CompletedTask.objects.all()
    task.delete()
    return redirect("/")