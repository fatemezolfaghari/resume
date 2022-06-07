from django.shortcuts import render

def cv_view(request):
    return render(request, 'cv/index.html')


def about_view(request):
    return render(request, 'cv/about.html')    