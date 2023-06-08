from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('booked_revenue/', views.booked_revenue_view, name='booked_revenue'),
]