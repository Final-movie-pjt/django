from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'movies/index.html')

def detail(request, pk):
    pass