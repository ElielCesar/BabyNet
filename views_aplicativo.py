from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def page_not_found(request, slug):
    return render(request, '404.html', status=404)
