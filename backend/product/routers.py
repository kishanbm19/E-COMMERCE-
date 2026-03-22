from .viewsets import Productviewset,Categoryviewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('categories',Categoryviewset),
router.register('products',Productviewset),
urlpatterns=router.urls