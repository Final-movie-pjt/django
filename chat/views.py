# chat/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Room

def index(request):
    rooms = Room.objects.filter(count_users__lte=0)
    for room in rooms:
        room.delete()
    rooms = Room.objects.all()
    context = { 
        'rooms': rooms,
    }
    return render(request, 'chat/index.html', context)

@login_required
def enter_room(request, room_pk):
    if request.user.is_authenticated:
        user = request.user
        room = Room.objects.get(pk=room_pk)
        room.count_users += 1
        room.save()
        context = {
            'room': room,
            'user': user,
        }
        return render(request, 'chat/room.html', context)

@login_required
def create(request):
    if request.user.is_authenticated:
        room_name = request.POST['roomname']
        room = Room.objects.create(room_name=room_name, count_users=0)
        return redirect('chat:room', room.pk)

