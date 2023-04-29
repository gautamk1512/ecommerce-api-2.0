from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet
from api import views

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.home, name='home'),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
]
