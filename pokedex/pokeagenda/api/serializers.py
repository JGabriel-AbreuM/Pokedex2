from pokeagenda.models import PokeAgenda
from rest_framework.serializers import ModelSerializer
import requests
import json
from random import randrange

class PokemonSerializer(ModelSerializer):
    class Meta:
        model = PokeAgenda
        fields = ["id", "nome", "imagem", "num_pokemon", "move1", "move2", "move3", "move4"]

class RegisterPokemonSerializer(ModelSerializer):
    class Meta:
        model = PokeAgenda
        fields = ["id", "imagem", "nome"]

    def create(self, validated_data):
        pokemon = validated_data["nome"]
        req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        dados = json.loads(req.text)

        ataques = []
        cont = 0
        if len(dados["moves"]) < 4:
            for _ in range(4):
                num = randrange(0, len(dados["moves"]))
                ataques.append(dados["moves"][num]["move"]["name"])
        else:
            while True:
                num = randrange(0, len(dados["moves"]))
                move = dados["moves"][num]["move"]["name"]
                if move not in ataques:
                    ataques.append(move)
                    cont  += 1

                if cont == 4:
                    break

        poke = PokeAgenda.objects.create(
            nome=validated_data["nome"],
            imagem=validated_data["imagem"],
            num_pokemon=dados["id"],
            move1=ataques[0],
            move2=ataques[1],
            move3=ataques[2],
            move4=ataques[3],
        )

        return poke