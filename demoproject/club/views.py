from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import club_members

def data(request):
    return render(request,'club.html')



def members(request):
  mymembers = club_members.objects.all().values()
  template = 'all_members.html'
  print("vinod mymbers are ", mymembers)
  context = {
    'mymembers': mymembers,
  }
  return render(request, template, context=context)

def details(request, id):
  mymember = club_members.objects.get(id=id)
  template = 'details.html'
  context = {
    'mymember': mymember,
  }
  return render(request,template,context=context) 