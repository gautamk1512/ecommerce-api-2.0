from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    # List all products or create a new product
    path('products/', include(router.urls)),
    # Retrieve, update or delete a specific product
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
