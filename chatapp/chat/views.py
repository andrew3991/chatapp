import json
import datetime
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import (
    ChatSession, ChatSessionMember, ChatSessionMessage, deserialize_user
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class ChatSessionView(APIView):
    """Manage Chat sessions."""

    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        """Get User Groups"""
        User = get_user_model()

        username = request.user.username
        user = User.objects.get(username=username)
        chat_session_all = ChatSession.objects.filter(owner=user)
        
        # Add uri of chat
        chat_sessions = [
                chat_session_uri.uri
                for chat_session_uri in chat_session_all
            ]


        usernames = []
        for chat in chat_session_all:
            if (len(chat.messages.all())>0):
                usernames.append(chat.messages.all().latest('create_date').user.username)
            else:
                usernames.append('')
        # Add last message of chat
        last_message = []
        for chat_session_uri in chat_session_all:
            if (len(chat_session_uri.messages.all())>0):
                last_message.append(chat_session_uri.messages.all().latest('create_date').message)
            else:
                last_message.append('')


        counter = 0
        counter_messages = []
        for chat_session_uri in chat_session_all:
            if (len(chat_session_uri.messages.all())>0):
                for stat in chat_session_uri.messages.all():
                    if(stat.status == 0 and stat.user.username != username):
                        counter = counter + 1
                counter_messages.append(counter)
            else:
                counter_messages.append(0)
        # Add status of message
        status = []
        for chat_session_uri in chat_session_all:
            if (len(chat_session_uri.messages.all())>0):
                status.append(chat_session_uri.messages.all().latest('create_date').status)
            else:
                status.append('')
        # Add chat title
        chat_titles = []
        for chat in chat_session_all:
            if(chat.title != ''):
                chat_titles.append(chat.title)
            else:
                for members in chat.members.all():
                    chat_titles.append(members.user.username)


        created_date = []

        
        for chat in chat_session_all:
            if (len(chat.messages.all())>0):
                date_str = chat.messages.all().latest('create_date').create_date
                date = datetime.datetime.strptime(str(date_str)[:19], '%Y-%m-%d %H:%M:%S')
                created_date.append(
                    str(date.date())[8:] + ' ' + str(date.date().strftime('%b')) + ' | ' + str(date.time())[:5]
                )
            else:
                created_date.append('')

        chats = zip(chat_sessions, chat_titles, last_message, status, usernames,counter_messages,created_date)
        

        #Chats where i am guest

        chat_session_all = ChatSessionMember.objects.filter(user=user)
        
        
        usernames_guest = []
        
        for chat in chat_session_all:
            if (len(chat.chat_session.messages.all())>0):
                usernames_guest.append(chat.chat_session.messages.all().latest('create_date').user.username)
            else:
                usernames_guest.append('')
        # Add uri of chat
        chat_sessions_guest = [
                chat_session_uri.chat_session.uri
                for chat_session_uri in chat_session_all
            ]
        # Add last message of chat
        last_message_guest = []
        for chat in chat_session_all:
            if (len(chat.chat_session.messages.all())>0):
                last_message_guest.append(chat.chat_session.messages.all().latest('create_date').message)
            else:
                last_message_guest.append('')

        # Add status of message
        status_guest = []
        for chat in chat_session_all:
            if (len(chat.chat_session.messages.all())>0):
                status_guest.append(chat.chat_session.messages.all().latest('create_date').status)
            else:
                status_guest.append('')
        # Add chat title

        chat_titles_guest = []
        for chat in chat_session_all:
            if(chat.chat_session.title != ''):
                chat_titles_guest.append(chat.chat_session.title)
            else:
                chat_titles_guest.append(chat.chat_session.owner.username)


        created_date_guest = []
        
        for chat in chat_session_all:
            if (len(chat.chat_session.messages.all())>0):
                date_str = chat.chat_session.messages.all().latest('create_date').create_date
                date = datetime.datetime.strptime(str(date_str)[:19], '%Y-%m-%d %H:%M:%S')
                created_date_guest.append(
                    str(date.date())[8:] + ' ' + str(date.date().strftime('%b')) + ' | ' + str(date.time())[:5]
                )
            else:
                created_date_guest.append('')


        counter_guest = 0
        counter_messages_guest = []
        for chat in chat_session_all:
            if (len(chat.chat_session.messages.all())>0):
                for stat in chat.chat_session.messages.all():
                    if(stat.status == 0 and stat.user.username != username):
                        counter_guest = counter_guest + 1
                counter_messages_guest.append(counter_guest)
            else:
                counter_messages_guest.append(0)

        chats_guest = zip(chat_sessions_guest, chat_titles_guest, last_message_guest, status_guest,usernames_guest,counter_messages_guest,created_date_guest)





        return Response({
            'chat_sessions': chat_sessions, 'chat_titles': chat_titles,'chats': chats,
            'chats_guest': chats_guest
        })


    def post(self, request, *args, **kwargs):
        """create a new chat session."""
        user = request.user
        chat_session = ChatSession.objects.create(owner=user)
        

        return Response({
            'status': 'SUCCESS', 'uri': chat_session.uri,
            'message': 'New chat session created'
        })

    def patch(self, request, *args, **kwargs):
        """Add a user to a chat session."""
        User = get_user_model()

        uri = kwargs['uri']
        username = request.data['username']
        user = User.objects.get(username=username)

        chat_session = ChatSession.objects.get(uri=uri)
        owner = chat_session.owner

        if owner != user:  # Only allow non owners join the room
            chat_session.members.get_or_create(
                user=user, chat_session=chat_session
            )

        owner = deserialize_user(owner)
        members = [
            deserialize_user(chat_session.user) 
            for chat_session in chat_session.members.all()
        ]
        members.insert(0, owner)  # Make the owner the first member

        return Response ({
            'status': 'SUCCESS', 'members': members,
            'message': '%s joined that chat' % user.username,
            'user': deserialize_user(user)
        })
    

class ChatSessionMessageView(APIView):
    """Create/Get Chat session messages."""

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """return all messages in a chat session."""
        User = get_user_model()

        uri = kwargs['uri']
        username = request.user.username
        user = User.objects.get(username=username)

        chat_session = ChatSession.objects.get(uri=uri)

        messages = [chat_session_message.to_json() 
            for chat_session_message in chat_session.messages.all()]


        username_title = ''
        if (chat_session.title == ''):
            if(user.username == chat_session.owner.username):
                username_title = chat_session.owner.username
            else:
                for members in chat_session.members.all():
                    username_title = members.user.username
        else:
            username_title = chat_session.title


        return Response({
            'id': chat_session.id, 'uri': chat_session.uri,
            'username_title':username_title,
            'messages': messages 
        })

    def post(self, request, *args, **kwargs):
        """create a new message in a chat session."""
        uri = kwargs['uri']
        message = request.data['message']

        user = request.user
        chat_session = ChatSession.objects.get(uri=uri)

        ChatSessionMessage.objects.create(
            user=user, chat_session=chat_session, message=message
        )

        return Response ({
            'status': 'SUCCESS', 'uri': chat_session.uri, 'message': message,
            'user': deserialize_user(user)
        })


class ChatGroupAddView(APIView):
    def get(self, request, *args, **kwargs):
        User = get_user_model()

        users = User.objects.all()

        users_list = []
        for user in users:
            if(request.user.username != user.username):
                users_list.append(user.username)
            

        return Response ({
            'status': 'SUCCESS', 'users_list': users_list
        })

    def post(self, request, *args, **kwargs):
        """create a new message in a chat session."""
        User = get_user_model()

        users = json.loads(request.data['users_list_selected'])
        user = request.user
        if (len(users)>1):
            if (request.data['chat_group_title']):
                title = request.data['chat_group_title']
        else:
            title = ''

        chat_session = ChatSession.objects.create(owner=user, title=title)
        owner = chat_session.owner

        for u in users:
            user = User.objects.get(username=u)
            chat_session.members.create(
                user=user, chat_session=chat_session
            )

        return Response ({
            'status': 'SUCCESS', 'uri': chat_session.uri
        })
        

    def patch(self, request, *args, **kwargs):
        """Add a user to a chat session."""
        uri = request.data['chat_uri']
        chat_session = ChatSession.objects.get(uri=uri)
        for message in chat_session.messages.all():
            if(message.user.username != request.user.username):
                if(message.status == 0):
                    message.status = 1
                    message.save()

        return Response ({
            'status': 'SUCCESS'
        })