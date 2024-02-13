from django.urls import path
from . import views

app_name = "vendor"
urlpatterns = [
    path("seller/",views.DashboardView.as_view(),name="dashboard"),

    path("manageproduct/",views.ManageProductView.as_view(),name="manageproduct"),
    path("addproduct/",views.AddProductView.as_view(),name="addproduct"),
    path("deleteproduct/<int:product_id>/",views.delete_product,name="deleteproduct"),


    path("manageorder/",views.ManageOrderView.as_view(),name="manageorder"),
]
