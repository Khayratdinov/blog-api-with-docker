from django.urls import include, path
from rest_framework import routers

from .views import (APISendCode, APISendToken, UserViewSet)


router = routers.DefaultRouter()

router.register('', UserViewSet, basename='user')


urlpatterns = [
    path('auth/signup/', APISendCode.as_view(), name='signup'),
    path('auth/token/', APISendToken.as_view(), name='get_token'),
    path('', include(router.urls)),
]