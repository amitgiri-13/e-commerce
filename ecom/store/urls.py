from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = (
    path("home/",views.IndexView.as_view(),name="home"),
    path("detail/",views.ProductDetailView.as_view(),name="productdetail"),
    path("signup/",views.signup,name="signup"),
    path("login/",auth_views.LoginView.as_view(template_name="store/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
)