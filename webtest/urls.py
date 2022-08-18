from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tests2/', views.test2, name='test2'),
    path('platform/', views.PMCtestView.as_view()),
    # path('getProvince/', views.getProvince),
    # path('getCity/', views.getCity),
    # path('getDistrict/', views.getDistrict),
]