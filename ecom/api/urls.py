from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'products',views.ProductViewSet,basename="products")
router.register(r'users',views.UserViewSet,basename="users")

urlpatterns = [
    path("",include(router.urls))
]