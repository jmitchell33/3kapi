from django.conf import settings
from rest_framework import routers
from django.urls import include, path, re_path
from . import views

router = routers.DefaultRouter()
router.register(r'eternal_powers', views.EternalPowerDetail, basename='eternal_powers_detail')
router.register(r'area', views.AreaDetail, basename='area_detail')
router.register(r'room', views.RoomDetail, basename='room_detail')
router.register(r'item', views.ItemDetail, basename='item_detail')
router.register(r'monster', views.MonsterDetail, basename='monster_detail')
router.register(r'crafting_components', views.CraftingComponentDetail, basename='crafting_component_detail')
router.register(r'satchel', views.CraftingSatchelDetail, basename='satchel_detail')

urlpatterns = router.urls