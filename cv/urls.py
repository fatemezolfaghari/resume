from django.urls import path
from cv.views import *

app_name = 'cv'

urlpatterns = [
    path('', cv_view, name='index'),
    path('about', about_view, name='about')
]

