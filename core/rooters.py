from rest_framework import routers

from account.views import CustomerViewSet
from store.views.api import CategoryViewSet, ProductViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register("category", CategoryViewSet, basename="category")
router.register("customer", CustomerViewSet, basename="customer")
router.register("product", ProductViewSet, basename="product")
router.register("order", OrderViewSet, basename="order")
