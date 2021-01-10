from django.urls import path
from . import views

app_name = "chatapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<str:room_name>/', views.room, name='room'),
    path('load/messages/', views.get_message, name='chat_message'),
    path('create/chat/', views.create_chat, name='create_chat'),
]