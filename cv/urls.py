from unicodedata import name
from django.urls import path
from cv.views import *

app_name = 'cv'

urlpatterns = [
    path('', cv_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('portfolio', portfolio_view, name='portfolio'),
    path('resume', resume_view, name='resume')
]

