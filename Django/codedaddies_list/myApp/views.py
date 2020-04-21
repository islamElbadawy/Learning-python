from django.shortcuts import render


# Rendering Home view
def home(request):
    return render(request, 'base.html')
