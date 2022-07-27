from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('platform/', views.TestPMCView.as_view()),
    path('getProvince/', views.getProvince),
    path('getCity/', views.getCity),
    path('getDistrict/', views.getDistrict),
]