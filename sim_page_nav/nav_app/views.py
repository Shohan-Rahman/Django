from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'nav_app/about.html')

def contact(request):
    return render(request,'nav_app/contact.html')