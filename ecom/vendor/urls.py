from django.urls import path
from . import views

app_name = "vendor"
urlpatterns = [
    path("seller/",views.DashboardView.as_view(),name="dashboard"),

    path("manageproduct/",views.ManageProductView.as_view(),name="manageproduct"),
    path("addproduct/",views.AddProductView.as_view(),name="addproduct"),
    path("deleteproduct/<int:product_id>/",views.delete_product,name="deleteproduct"),
    path("editproduct/<int:product_id>/",views.EditProductView.as_view(),name="editproduct"),


    path("manageorder/",views.ManageOrderView.as_view(),name="manageorder"),
    path("deleteorder/<int:order_id>/",views.delete_order,name="deleteorder"),
    path("dispatchorder/<int:order_id>/",views.dispatch_order,name="dispatchorder"),
    
    path("print/<int:pk>/",views.ShippingView.as_view(),name="print"),

    path("setting/",views.SettingView.as_view(),name="setting"),
]
