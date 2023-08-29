from django.views.decorators.csrf import csrf_exempt
from .models import Task
from django.http import HttpResponse


@csrf_exempt
def list_create_tasks(request):
    if request.method == 'POST':
        task_name=request.POST.get('task')
        task1=Task.objects.create(name=task_name)
        task=Task.objects.get(name=task_name)
        return HttpResponse(f"Task Created: '{task_name}'")
