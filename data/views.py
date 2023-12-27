import copy
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status, mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from . import models, serializers

class EternalPowerDetail(viewsets.ModelViewSet):
    queryset = models.Eternal_Powers.objects.all()
    serializer_class = serializers.EternalPowersSerializer 

    # We will attempt to update first, if the character/eternal doesn't exist we'll create it
    def create(self, request, *args, **kwargs):
        partial = True
        character = request.data.get('character')
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

class RoomDetail(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer

    def create(self, request, *args, **kwargs):
        partial = True
        new_data = copy.deepcopy(request.data)
        area_name = new_data.get('parent_area')
        try:
            parent_pk = models.Area.objects.filter(name=area_name).first().pk
            new_data['parent_area'] = parent_pk
            serializer = self.get_serializer(data=new_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ObjectDoesNotExist:
            new_data['parent_area'] = None
            serializer = self.get_serializer(data=new_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class MonsterAttackDetail(viewsets.ModelViewSet):
    queryset = models.Monster_AttackType.objects.all()
    serializer_class = serializers.MonsterAttackSerializer

class CraftingComponentDetail(viewsets.ReadOnlyModelViewSet):
    queryset = models.Crafting_Component.objects.all()
    serializer_class = serializers.CraftingComponentSerializer

class CraftingSatchelDetail(viewsets.ModelViewSet):
    queryset = models.Crafting_Satchel.objects.all()
    serializer_class = serializers.Crafting_Satchel 

    # We will attempt to update first, if the character + component type + quantity doesn't exist we'll create it
    def create(self, request, *args, **kwargs):
        partial = True
        character = request.data.get('character')
        component = request.data.get('component')
        quality = request.data.get('quality')
        try:
            instance = models.Crafting_Satchel.objects.get(character=character, component=component, quality=quality)
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