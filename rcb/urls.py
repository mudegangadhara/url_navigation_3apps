from django.urls import path
from rcb.views import *

app_name='virat'

urlpatterns=[
    path('virat/',virat,name='virat')
]