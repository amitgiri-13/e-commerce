from django.urls import path
from . import views

app_name = "vendor"
urlpatterns = [
    path("seller/",views.DashboardView.as_view(),name="dashboard"),
    path("manageproduct/",views.ManageProductView.as_view(),name="manageproduct"),
    path("manageorder/",views.ManageOrderView.as_view(),name="manageorder"),
]
