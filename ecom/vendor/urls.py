from django.urls import path
from . import views

app_name = "vendor"
urlpatterns = [
    path("seller/",views.DashboardView.as_view(),name="dashboard"),
]
