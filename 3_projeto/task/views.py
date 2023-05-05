from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from .forms import CreateTask


def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'task/index.html', context)


def tasks_pending(request):
    tasks_pending = Post.objects.filter(status='pending')
    return render(request, 'task/pending.html', 
                  {'title': 'Tasks Pending', 'tasks_pending': tasks_pending})


def create_task(request):
    if request.method == 'POST':
        form = CreateTask(data=request.POST)
        if form.is_valid():
            breakpoint()
            form.save()
            author = form.cleaned_data.get('author')
            messages.success(request, f'Tarefa criada com sucesso, {author}!')
            return redirect('task-index')
    else:
        form = CreateTask()
    return render(request, 'task/create.html', {'form': form})
