from .viewsets import Productviewset,Categoryviewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('categories',Categoryviewset,basename='categories'),
router.register('products',Productviewset,basename='product-detail'),
urlpatterns=router.urls