from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from chatapp.models import *

# Create your views here.


def get_minute(minute):
    if minute < 10:
        return "0{}".format(minute)
    return minute


@login_required
def index(request):
    chats = request.user.chats.all().order_by('-update_time')[:30]
    return render(request, 'chatapp/index.html', context={"chats": chats, "current_user": request.user})

@login_required
def get_message(request):
    chat_id = request.POST.get('chat_id', None)
    if chat_id is None:
        return JsonResponse({"status": "Error, chat_id is required"}, status=401)
    
    chat = list(Chat.objects.filter(id=chat_id, members__in=[request.user]))[0]
    messages = list(Message.objects.filter(chat=chat))[:100]

    payload = []
    for m in messages:
        payload.append({
            "message_text": m.message_text,
            "sender": m.sender.id,
            "send_time": "{}:{}".format(m.send_time.hour, get_minute(m.send_time.minute))
        })

    return JsonResponse({"messages": payload}, status=200)

@login_required
def create_chat(request):
    target_user_id = request.POST.get('target_user_id', None)
    target_user = User.objects.get(id=target_user_id)

    chat = Chat.objects.filter(members__in=[request.user]).filter(members__in=[target_user])
    if chat.count() == 0:
        c = Chat()
        c.save()
        c.members.add(target_user)
        c.members.add(request.user)
        c.save()
        return JsonResponse({"chat_id": c.id}, status=201)
    return JsonResponse({"chat_id": chat[0].id}, status=200)
    

def room(request, room_name):
    return render(request, 'chatapp/room.html', {
        'room_name': room_name
    })