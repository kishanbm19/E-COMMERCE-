from .viewsets import Productviewset,Categoryviewset,CartItemview,Cartview,OrderItemview,Orderview
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('categories',Categoryviewset),
router.register('products',Productviewset),
router.register('cart',Cartview),
router.register('cartitems',CartItemview),
router.register('Order',Orderview),
router.register('orderitems',OrderItemview)

urlpatterns=router.urls