from django.urls import path

from . import views

urlpatterns = (
    path("home/",views.IndexView.as_view(),name="home"),
    path("detail/",views.ProductDetailView.as_view(),name="productdetail"),
    path("signup/",views.signup,name="signup"),
)