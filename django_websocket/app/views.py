from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def room(request, room_name):
    return render(request, "app/room.html", {"room_name": room_name})