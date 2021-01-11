from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import CreateTaskForm, UpdateTaskForm, UserRegisterForm
from .models import Task

# Create your views here.
def home(request):
    context = {'title': 'Home'}
    return render(request, 'users/home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'title': 'Register', 'form': form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            description = form.cleaned_data['description']
            due_date = form.cleaned_data['due_date']
            priority = form.cleaned_data['priority']

            user = request.user
            task = Task(description=description, due_date=due_date, priority=priority, user=user)

            task.save()
            return redirect('profile')
    else:
        form = CreateTaskForm()

    tasks = Task.objects.filter(user=request.user)

    context = {'title': 'Profile', 'form': form, 'tasks': tasks}
    return render(request, 'users/profile.html', context)

def complete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    context = {'title': 'Complete'}
    return render(request, 'users/complete.html', context)

def update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            task.description = form.cleaned_data['description']
            task.priority = form.cleaned_data['priority']
            task.due_date = form.cleaned_data['due_date']
            task.save()
            
            return redirect('profile')
    else:
        form = UpdateTaskForm()
    
    context = {'title': 'Update', 'task': task, 'form': form}
    return render(request, 'users/update.html', context)

def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    context = {'title': 'Delete'}
    return render(request, 'users/delete.html', context)