from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import PasswordResetConfirmForm
from . import views

urlpatterns = (
    path("signup/",views.signup,name="signup"),
    path("login/",views.CustomLoginView.as_view(template_name="store/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    
    path("editprofile/",views.edit_profile,name="editprofile"),

    path("profile/",views.ProfileView.as_view(),name="profile"),
    path("home/",views.IndexView.as_view(),name="home"),
    path("search/",views.search_items,name="search"),
    path("newarrivals/",views.NewArrivalView.as_view(),name="new_arrivals"),
    path("detail/<int:pk>/",views.ProductDetailView.as_view(),name="product_detail"),
    path("reviews/",views.ReviewView.as_view(),name="reviews"),

    path("mycart/",views.MyCartView.as_view(),name="my_carts"),
    path("addtocart/<int:product_id>/",views.add_to_cart,name="add_to_cart"),
    path("removefromcart/<int:item_id>/",views.remove_from_cart,name="remove_from_cart"),

    path("orders/",views.OrderView.as_view(),name="orders"),
    path("buynow/<int:product_id>/",views.buynow,name="buynow"),
    path("cancel/<int:order_id>/",views.cancel_order,name="cancelorder"),
    path("orderdetail/<int:pk>",views.OrderDetailView.as_view(),name="orderdetail"),
    path("payment/<int:pk>",views.PaymentView.as_view(),name="payment"),
    path("purchase/",views.PurchaseView.as_view(),name="purchase"),
    path("return/",views.ReturnView.as_view(),name="return"),

    path("passwordreset/",views.CustomPasswordResetView.as_view(template_name="store/passwordreset.html"),name="password_reset"),
    path("passwordreset/done/",auth_views.PasswordResetDoneView.as_view(template_name="store/passwordresetdone.html"),name="password_reset_done"),
    path("passwordreset/confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="store/passwordresetconfirm.html"),name="password_reset_confirm"),
    path("passwordreset/complete/",auth_views.PasswordResetCompleteView.as_view(template_name="store/passwordresetcomplete.html"),name="password_reset_complete"),
)