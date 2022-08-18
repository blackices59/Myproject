from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import RelationshipTable


# def home(request):
#     return render(request, 'tests/test2.html')


# def t2(request):
#     return render(request, 'tests/test2.html')


# 获取商标信息
def getBrand(request):
    # 读取relationship值为空值的信息（即为brand信息）
    brands = RelationshipTable.objects.filter(relationship__isnull=True)
    res = []
    for i in brands:
        res.append([i.id, i.info])

    return JsonResponse({"brands": res})


# 获取平台信息
def getPlatform(request):

    platform_id = request.GET.get('platform_id')
    platforms = RelationshipTable.objects.filter(relationship_id=platform_id)
    res = []
    for i in platforms:
        res.append([i.id, i.info])

    return JsonResponse({"platforms": res})


# 获取车型代码信息
def getCarModel(request):

    carmodel_id = request.GET.get('carmodel_id')
    carmodels = RelationshipTable.objects.filter(relationship_id=carmodel_id)
    res = []
    for i in carmodels:
        res.append([i.id, i.info])

    return JsonResponse({"carmodels": res})


# 获取发动机型号信息
def getEngine(request):

    engine_id = request.GET.get('engine_id')
    engines = RelationshipTable.objects.filter(relationship_id=engine_id)
    res = []
    for i in engines:
        res.append([i.id, i.info])

    return JsonResponse({"engines": res})


# 获取变速箱型号信息
def getGearBox(request):

    gearbox_id = request.GET.get('gearbox_id')
    gearboxs = RelationshipTable.objects.filter(relationship_id=gearbox_id)
    res = []
    for i in gearboxs:
        res.append([i.id, i.info])

    return JsonResponse({"gearboxs": res})

# 获取排放法规信息
def getEmissionRegulation(request):

    emissionRegulation_id = request.GET.get('emissionRegulation_id')
    emissionRegulations = RelationshipTable.objects.filter(relationship_id=emissionRegulation_id)
    res = []
    for i in emissionRegulations:
        res.append([i.id, i.info])

    return JsonResponse({'emissionRegulations': res})


def home(request):
    a = RelationshipTable.objects.filter()
    return render(request, 'tests/test_finish.html', {'string': a})
