from community.models import Review
from django.shortcuts import render

# Create your views here.

def create(request):
    pass


def community_detail(request, pk):
    review = Review.objects.get(pk=pk)