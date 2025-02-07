from django.urls import path
from .views import chat_assistant,index

urlpatterns = [
    path('', index, name='index'),
    path('chat/', chat_assistant, name='chat_assistant'),
]

