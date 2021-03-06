from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf.urls import url, include
from rest_framework.authtoken import views as drf_views

from django.urls import path

from . import views

# Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#   class Meta:
#      model = User
#     fields = ['username', 'email', 'password']

# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#   queryset = User.objects.all()
#  serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("about_us", views.about_us, name="about_us")
]


#path('', include(router.urls)),
#path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
