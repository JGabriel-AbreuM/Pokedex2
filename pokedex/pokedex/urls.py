"""pokedex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.api.views import RegisterAPI, UserAPI, LoginAPI, OTP_API
from pokeagenda.api.views import RegisterPokemonAPI, PokemonAPI
from knox import views as knox_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers 
from django.urls.conf import include

router = routers.DefaultRouter()
router.register(r'pokeagenda', PokemonAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/user/', UserAPI.as_view()),
    path('api/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/login/', LoginAPI.as_view()),
    path('api/otp/', OTP_API.as_view()),
    path('api/pokeagenda/register', RegisterPokemonAPI.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
