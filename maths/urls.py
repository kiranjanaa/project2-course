from django.urls import path
from maths.views import *
urlpatterns=[
    path('typesofcourse/',typesofcourse,name='typesofcourse'),
]