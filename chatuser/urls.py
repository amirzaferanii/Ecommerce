from django.urls import path
from . import views

app_name = 'chatuser'

urlpatterns = [

      path('<str:slug>', views.ChatUserView.as_view(), name='profile_chat_user'),
      path('list/<slug:slug>', views.ChatListView.as_view(), name='profile_chat_list'),
]