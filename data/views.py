from django.conf import settings

from rest_framework import status, mixins, viewsets
from rest_framework.authentication import SessionAuthentication

from . import models, serializers

class EternalPowerDetail(viewsets.ModelViewSet):
    queryset = models.Eternal_Powers.objects.all()
    serializer_class = serializers.EternalPowersSerializer

class ItemDetail(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

class MonsterDetail(viewsets.ModelViewSet):
    queryset = models.Monster.objects.all()
    serializer_class = serializers.MonsterSerializer

class AreaDetail(viewsets.ModelViewSet):
    queryset = models.Area.objects.all()
    serializer_class = serializers.AreaSerializer

class MonsterAttackDetail(viewsets.ModelViewSet):
    queryset = models.Monster_AttackType.objects.all()
    serializer_class = serializers.MonsterAttackSerializer