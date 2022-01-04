from django import http
from pokeagenda.models import PokeAgenda
from .serializers import PokemonSerializer, RegisterPokemonSerializer
from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

class RegisterPokemonAPI(generics.GenericAPIView):
    serializer_class = RegisterPokemonSerializer
    permissions_classes = IsAuthenticated

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            return Response({
                "pokemon": PokemonSerializer(user, context=self.get_serializer_context()).data
            })
        except:
            return Response({
                "erro": "Algo de errado que não está certo aconteceu"
            })

class PokemonAPI(ModelViewSet):
    queryset = PokeAgenda.objects.all()
    permissions_classes = IsAuthenticated
    serializer_class = PokemonSerializer
    http_method_names = ["get", "head"]