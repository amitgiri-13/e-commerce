from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = (
    path("profile/",views.ProfileView.as_view(),name="profile"),
    path("home/",views.IndexView.as_view(),name="home"),
    path("newarrivals/",views.NewArrivalView.as_view(),name="new_arrivals"),
    path("mycart/",views.MyCartView.as_view(),name="my_carts"),
    path("detail/<int:pk>/",views.ProductDetailView.as_view(),name="product_detail"),
    path("signup/",views.signup,name="signup"),
    path("login/",auth_views.LoginView.as_view(template_name="store/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("addtocart/<int:product_id>/",views.add_to_cart,name="add_to_cart"),
    path("removefromcart/<int:item_id>/",views.remove_from_cart,name="remove_from_cart"),
    path("search/",views.search_items,name="search"),
    path("orders/",views.OrderView.as_view(),name="orders"),
    path("buynow/<int:product_id>/",views.buynow,name="buynow"),
)