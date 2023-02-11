from django.http import HttpResponse
from .models import Task

def list_create_tasks(request):
    if request.method == 'GET':
        tasks=Task.objects.all().order_by('name').values_list('name',flat=True)
        return HttpResponse('\n'.join(tasks))


def count_tasks(request):
    if request.method == 'GET':
        count=Task.objects.all().count()
        response=f"You have '{count}' tasks to do"
        return HttpResponse(response)
