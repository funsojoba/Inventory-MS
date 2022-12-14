from rest_framework import routers

from .views import ProductViewed, CartViewset

router = routers.DefaultRouter()

router.register(r'products', ProductViewed)
router.register(r'cart', CartViewset, basename='cart')

urlpatterns = router.urls