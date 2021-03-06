import email
from django.shortcuts import render

def cv_view(request):
    return render(request, 'cv/index.html')


def about_view(request):
    return render(request, 'cv/about.html')   


def contact_view(request):
    return render(request, 'cv/contact.html')


def portfolio_view(request):
    return render(request, 'cv/portfolio.html')    


def resume_view(request):
    return render(request, 'cv/resume.html')  


def contact_store_view(request):
    data = {
        'message': "Message sent successfully"
    }
    return render(request, 'cv/contact.html', context= data)