from rest_framework import routers

from .viewsets import HouseViewsets

app_name = 'house'

router = routers.DefaultRouter()
router.register('houses', HouseViewsets)