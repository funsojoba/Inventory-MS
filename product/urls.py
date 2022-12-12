from rest_framework import routers

from .views import ProductViewed

router = routers.DefaultRouter()

router.register(r'products', ProductViewed)

urlpatterns = router.urls