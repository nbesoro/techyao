from rest_framework import routers

from account.views import CustomerViewSet
from store.views.api import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register("category", CategoryViewSet, basename="category")
router.register("customer", CustomerViewSet, basename="customer")
router.register("product", ProductViewSet, basename="product")
