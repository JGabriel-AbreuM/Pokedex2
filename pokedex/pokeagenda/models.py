from django.db import models
import uuid
# Create your models here.
class PokeAgenda(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length=999, blank=False, null=False)
    imagem = models.ImageField(upload_to="images/")
    num_pokemon = models.IntegerField(blank=False, null=False)
    move1 = models.CharField(max_length=999, blank=False, null=False)
    move2 = models.CharField(max_length=999, blank=False, null=False)
    move3 = models.CharField(max_length=999, blank=False, null=False)
    move4 = models.CharField(max_length=999, blank=False, null=False)

    def __str__(self):
        return self.nome