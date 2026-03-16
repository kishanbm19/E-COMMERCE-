from .viewsets import Productviewset,Categoryviewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('domain',Categoryviewset,basename='categories'),
router.register('item',Productviewset,basename='product-detail'),
urlpatterns=router.urls