from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'index.html')

def profile(request):
  context = {
     "Fullname" : "Juan Dela Cruz",
     "Skills" : ["Eating", "Programming", "BasketBall"]
  }
  return render(request, 'profile.html', context)
