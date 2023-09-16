from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# this is the part of the website accessible only to admin
@login_required
def dashboard(request):
    
    context={}

    return render(request, 'website/dashboard.html', context)



# this is part of the website accessible to everyone
def base(request):
    
    context = {
    }

    return render(request, 'website/landing.html', context)