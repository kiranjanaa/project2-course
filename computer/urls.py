from django.urls import path
from computer.views import *
urlpatterns=[
    path('typesofcourse/',typesofcourse,name='typesofcourse'),
]