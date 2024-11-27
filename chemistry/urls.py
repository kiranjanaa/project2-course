from django.urls import path
from chemistry.views import *
urlpatterns=[
    path('typesofcourse/',typesofcourse,name='typesofcourse'),
]