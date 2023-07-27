from django.shortcuts import render
from django.http import HttpResponse

posts= [
    {
        'author':'CoreyMS',
        'title' :'Blog post 1',
        'content':'First post content',
        'date_posted':'August 27, 2018'
    },
    {  'author':'Jane Done',
        'title' :'Blog post 2',
        'content':'Second post content',
        'date_posted':'August 28, 2018' 
    }

]


def home(request):
    context={
        'posts':posts
    }
    return render(request,'home.html', context)

def about(request):
    return render(request,'about.html',{'title':'About'})