from django.shortcuts import render,HttpResponse

# Create your views here.
def homepage(request):
    return render(request,'home.html')

def shoppage(request):
    return render(request,'shop.html')

def videopage(request):
    return render(request,'videos.html')