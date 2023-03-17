from django.urls import path
from csk.views import *

app_name='dhoni'

urlpatterns=[
    path('dhoni/',dhoni,name='dhoni')
]