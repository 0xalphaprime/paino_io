from django.shortcuts import render
from .models import DashboardView, BookedRevenue


# views

def dashboard_view(request):
    content_objects = DashboardView.objects.all()  # Get all objects
    return render(request, 'dashboard.html', {'content_objects': content_objects})


def booked_revenue_view(request):
    content_objects = BookedRevenue.objects.all()  # Get all objects
    return render(request, 'booked_revenue_zb.html', {'content_objects': content_objects})