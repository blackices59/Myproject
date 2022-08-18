from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # path('t2/', views.t2),
    # path('', views.PlatformView.as_view()),

    # 将自关联获取函数分发到地址中
    # 获取车辆商标信息
    path('getBrand/', views.getBrand),
    # 获取车型平台
    path('getPlatform/', views.getPlatform),
    # 获取车型代码
    path('getCarModel/', views.getCarModel),
    # 获取发动机型号
    path('getEngine/', views.getEngine),
    # 获取变速箱型号
    path('getGearBox/', views.getGearBox),
    # 获取排放法规
    path('getEmissionRegulation/', views.getEmissionRegulation),

    path('', views.home)
    # url(r'^addr/(\d+)$', views.addrAPI, name='Addr'),

]
