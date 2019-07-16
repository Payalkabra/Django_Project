from django.urls import path
from . import views

urlpatterns = [
    path(r'website/',views.website , name = 'website'),
    path(r'my_custom/' ,views.my_custom , name = 'my_custom'),
    
]