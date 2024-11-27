from django.urls import path
from physics.views import *
urlpatterns=[
    path('typesofcourse/',typesofcourse,name='typesofcourse'),
]