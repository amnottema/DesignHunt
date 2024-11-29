from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/<int:user_id>/', views.portfolio_detail, name='portfolio_detail'),
]