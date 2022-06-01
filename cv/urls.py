from django.urls import path
from cv.views import *

app_name = 'cv'

urlpatterns = [
    path('', cv_view, name='cv')
]
