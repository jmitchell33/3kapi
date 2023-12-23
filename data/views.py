from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status, mixins, viewsets
from rest_framework.authentication import SessionAuthentication

from . import models, serializers

class EternalPowerDetail(viewsets.ModelViewSet):
    queryset = models.Eternal_Powers.objects.all()
    serializer_class = serializers.EternalPowersSerializer 

    # We will always use update, if the character/eternal doesn't exist we'll create it
    def update(self, request, *args, **kwargs):
        partial = True
        character = kwargs.pop('character')
        try:
            instance = models.Eternal_Powers.objects.get(character=character)
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            queryset = self.filter_queryset(self.get_queryset())
            if queryset._prefetch_related_lookups:
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance,
                # and then re-prefetch related objects
                instance._prefetched_objects_cache = {}
                prefetch_related_objects([instance], *queryset._prefetch_related_lookups)

            return Response(serializer.data)
        except ObjectDoesNotExist:
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