from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .serializers import UserSerializer

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
	HTTP_203_NON_AUTHORITATIVE_INFORMATION,
	HTTP_201_CREATED,
	HTTP_202_ACCEPTED,
)

from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRUDView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        context = {}
        username = request.data.get('username')
        password = request.data.get('password')
        UserModel = get_user_model()
        users = None
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            users = None
        else:
            if user.check_password(password):
                users = user
        if users:
            # token, created = Token.objects.get_or_create(user=users)
            context['status'] = 1
            context['response'] = 'Success'
			# context['token'] = token.key
            context['id'] = users.pk
        else:
            context['status'] = 0
            context['response'] = 'Error'
            context['message'] = 'Invalid username or password'
            return Response(context,status=HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            
        return Response(context,status=HTTP_202_ACCEPTED)
