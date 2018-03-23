from django.shortcuts import render
from django.db import models
from django.utils import timezone
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import MyModelTest

def add_records(request):
    print(request.get_full_path)
    n = 10000
    for i in range(0, n):
        number = i + 1
        print("Number: " + str(number))
        contentA = "AA" + str(number)
        contentB = "BB" + str(number)
        MyModelTest.objects.create(contentA=contentA, contentB=contentB)
    return HttpResponse(str("All work OK"))

def delete_all_records(request):
    print(request.get_full_path)
    MyModelTest.objects.order_by('pk').delete()
    return render(request, 'prilogenie111/deleteOK.html', {})

