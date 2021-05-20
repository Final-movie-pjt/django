from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth import get_user_model


# Create your views here.
def signup(request):
    if request.method == 'POST':
        pass
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }

    return render(request, 'accounts/form.html', context)
