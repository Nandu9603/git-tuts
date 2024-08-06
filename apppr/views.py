from django.shortcuts import render
def contact(request):
    return render(request,'contact.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')

# Create your views here.
