from django.urls import path
from .import views 

app_name="club"
urlpatterns = [
    # path('', views.home, name='club'), 
    path('data/', views.data, name='data'),
    path('custmer-info/', views.members, name='getdata'),
    path('details/<int:id>', views.details, name='details'),
]    
   