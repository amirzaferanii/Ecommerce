from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Message
from Account.models import User
from django.db.models import OuterRef, Subquery


class ChatUserView(View):
    def get(self, request, slug):
        user = get_object_or_404(User, slug=slug)
        messages = Message.objects.filter(
            (Q(receiver=user) & Q(sender=request.user)) |(Q(receiver=request.user) & Q(sender=user))).order_by('timestamp')
        return render(request, 'chat_user/chat.html', context={'user': user, 'messages': messages,})


    def post(self, request, slug):
        user = get_object_or_404(User, slug=slug)
        content = request.POST.get('content')
        messages = Message.objects.create(content=content, receiver=user,sender=request.user)
        messages.save()
        return redirect('chatuser:profile_chat_user', slug=slug)


class ChatListView(View):
    def get(self, request, slug):
        user = User.objects.get(slug=slug)
        last_message_subquery = Message.objects.filter(sender=OuterRef('sender'),receiver=request.user).order_by('-timestamp').values('id')[:1]
        last_message_send = Message.objects.filter(receiver=OuterRef('receiver'),sender=user).order_by('-timestamp').values('id')[:1]
        last_messages = Message.objects.filter(id__in=Subquery(last_message_subquery)).order_by('-timestamp')
        last_messages_s = Message.objects.filter(id__in=Subquery(last_message_send)).order_by('-timestamp')
        return render(request, 'chat_user/chat_list.html', context={'chats': last_messages, 'chat_send': last_messages_s,'user': user})