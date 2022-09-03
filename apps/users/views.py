import secrets
import string
# ============================================================================ #
from rest_framework import  status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
# ============================================================================ #
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
# ============================================================================ #
from .models import User
from .serializers import (
                          EmailTokenSerializer, TokenObtainPairSerializer,
                          UserSerializer)



# ================================ USERVIEWSET =============================== #


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'username'

    @action(methods=['get', 'patch'],
            detail=False,
            permission_classes=(IsAuthenticated,),
            url_path='me',)

    def user_data(self, request):
        if request.method == 'GET':
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PATCH':
            serializer = UserSerializer(
                request.user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            if request.user.is_user:
                serializer.save()
            else:
                serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)



# ================================ APISENDCODE =============================== #

class APISendCode(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        confirmation_code = ''.join(
            secrets.choice(
                string.ascii_uppercase + string.digits) for _ in range(9))
        serializer = EmailTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            username=serializer.validated_data['username'],
            confirmation_code=confirmation_code
        )
        email = EmailMessage('Saytimizda royxattan otkaniz ushin rahmat ',
                             f'accauntizni activ qilish ushin code:'
                             f'{confirmation_code}',
                             to=[serializer.validated_data['email']],
                             )
        email.send()
        return Response(serializer.data,
                        status=status.HTTP_200_OK)



# =============================== APISENDTOKEN =============================== #

class APISendToken(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(
            User, username=serializer.validated_data['username']
        )

        if serializer.validated_data['confirmation_code'] == (
                user.confirmation_code):
            token = RefreshToken.for_user(user).access_token
            return Response({'token': str(token)}, status=status.HTTP_200_OK)
        return Response(
            {'Royxattan otishda xatolik': 'siz kiritgan code xato'},
            status=status.HTTP_400_BAD_REQUEST)