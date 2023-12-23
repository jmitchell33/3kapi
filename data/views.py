from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status, mixins, viewsets
from rest_framework.authentication import SessionAuthentication

from . import models, serializers

class EternalPowerDetail(viewsets.ModelViewSet):
    queryset = models.Eternal_Powers.objects.all()
    serializer_class = serializers.EternalPowersSerializer 

    # We will always use update, if the character/eternal doesn't exist we'll create it
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        


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