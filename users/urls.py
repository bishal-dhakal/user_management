from django.urls import path

from .views import DoctorDashboardView, create_user

urlpatterns = [
    path("", create_user, name="login"),
    path("dashboard", DoctorDashboardView.as_view(), name="dashboard"),
]
