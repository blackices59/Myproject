from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import PlatformModelCode
from .serializers import PlatformModelCodeSerializer


def home(request):
    return render(request, 'tests/home.html')


def test2(request):
    return render(request, 'tests/test2.html')


# # 获取车型信息
# def getProvince(request):
#     # 获取所有车型平台
#     provinces = PlatformModelCode.objects.filter(pid__isnull=True)
#     res = []
#     for i in provinces:
#         res.append([i.id, i.data])
#     return JsonResponse({"车型平台": res})
#
#
# # 获取车型代码
# def getCity(request):
#     model_id = request.GET.get('model_id')
#     # 获取当车型代码信息
#     models = PlatformModelCode.objects.filter(pid_id=model_id)
#     res = []
#     for i in models:
#         res.append([i.id, i.data])
#     return JsonResponse({"车型代码": res})
#
#
# # 获取车型code
# def getDistrict(request):
#     code_id = request.GET.get('code_id')
#     # 获取当前市的所有县
#     codes = PlatformModelCode.objects.filter(pid_id=code_id)
#     res = []
#     for i in codes:
#         res.append([i.id, i.data])
#     return JsonResponse({'车型code': res})

class PMCtestView(APIView):
    def get(self, request):

        pid_id = request.GET.get('pid_id')

        if pid_id:
            info = PlatformModelCode.objects.filter(pk=pid_id).first()
            infos = info.beyond

        else:
            infos = PlatformModelCode.objects.filter(pid__isnull=True).all()

        info_ser = PlatformModelCodeSerializer(infos, many=True)

        return Response({'code': 200, 'platformlist': info_ser.data})
