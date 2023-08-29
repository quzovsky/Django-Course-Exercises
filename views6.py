from django.shortcuts import render, HttpResponse
from .models import Musician, Album
from django.views import View


class Musician_list(View):
    def get(self,request):
        list=Musician.objects.values_list('name',flat=True).order_by('name')
        return HttpResponse(list)