from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def task_list(request):
    # משיכת כל המשימות ממסד הנתונים
    tasks = Task.objects.all()

    # שליחת המשימות לדף ה-HTML
    return render(request, 'tasks/task_list.html', {'tasks': tasks})