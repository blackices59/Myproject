from django.http import JsonResponse
from django.shortcuts import render
from django.forms import ModelForm

from . import models


# def home(request):
#     return render(request, 'tests/test2.html')


# def t2(request):
#     return render(request, 'tests/test2.html')


# 获取商标信息
def getBrand(request):
    # 读取relationship值为空值的信息（即为brand信息）
    brands = models.RelationshipTable.objects.filter(relationship__isnull=True)
    res = []
    for i in brands:
        res.append([i.id, i.info])

    return JsonResponse({"brands": res})


# 获取平台信息
def getPlatform(request):

    platform_id = request.GET.get('platform_id')
    platforms = models.RelationshipTable.objects.filter(relationship_id=platform_id)
    res = []
    for i in platforms:
        res.append([i.id, i.info])

    return JsonResponse({"platforms": res})


# 获取车型代码信息
def getCarModel(request):

    carmodel_id = request.GET.get('carmodel_id')
    carmodels = models.RelationshipTable.objects.filter(relationship_id=carmodel_id)
    res = []
    for i in carmodels:
        res.append([i.id, i.info])

    return JsonResponse({"carmodels": res})


# 获取发动机型号信息
def getEngine(request):

    engine_id = request.GET.get('engine_id')
    engines = models.RelationshipTable.objects.filter(relationship_id=engine_id)
    res = []
    for i in engines:
        res.append([i.id, i.info])

    return JsonResponse({"engines": res})


# 获取变速箱型号信息
def getGearBox(request):

    gearbox_id = request.GET.get('gearbox_id')
    gearboxs = models.RelationshipTable.objects.filter(relationship_id=gearbox_id)
    res = []
    for i in gearboxs:
        res.append([i.id, i.info])

    return JsonResponse({"gearboxs": res})


# 获取排放法规信息
def getEmissionRegulation(request):

    emissionRegulation_id = request.GET.get('emissionRegulation_id')
    emissionRegulations = models.RelationshipTable.objects.filter(relationship_id=emissionRegulation_id)
    res = []
    for i in emissionRegulations:
        res.append([i.id, i.info])

    return JsonResponse({'emissionRegulations': res})


def home(request):
    a = models.RelationshipTable.objects.all()
    info_hb = {
        'CN100平台': {
            'CN100V': ['N15A', '6MT', 'CN6b'],
            'CN110PPS': ['N15A', '5MT', 'CN6a/CN6b'],
            'CN110V': [('N15A', '5MT/6MT', 'CN6a/CN6b'), ('N12', '5MT', 'CN6b')],
            'CN112': ['N12', 'MT', 'CN6b'],
            'CN115': ['N15A', '6MT', 'CN6a/CN6b'],
            'CN120S': [('N15T', 'MT', 'CN6b'), ('N15A', '6MT', 'CN6a/CN6b')],
            'CN150M': [('N15A', '5MT/6MT', 'CN6b'), ('N15T', 'MT', 'CN6b')],
            'CN150V': ['N15T', 'MT', 'CN6a/CN6b'],
        },
        'N平台': {
            'N111': ['N12', 'MT', '无'],
            'N111PPS': ['N12', 'MT', '无'],
            'N300L': [('B15', 'MT/5MT', 'CN6b'), ('N15A', '5MT', '无')],
            'N300PPS': [('B15', 'MT/5MT', 'CN6b'), ('N15A/N12', '5MT', 'CN6b')],
            'N310': ['N12', '5MT', 'CN6b'],
            'N350': [('B15', 'MT', 'CN6b'), ('B15', '5MT', 'CN6a/CN6b'), ('N15A', '5MT', '无'),
                     ('LJ1.8', '5MT', 'CN6a/CN6b'), ('LJ1.8', 'MT', 'CN6b')],
        },
    }
    return render(request, 'tests/test_finish.html', {'string': a, 'info': info_hb})


class StudentList(ModelForm):
    class Meta:
        model = models.Student  # 对于的Model中的类
        fields = "__all__"  # 字段
        exclude = None  # 排除的字段
        labels = None  # 提示信息
        help_texts = None  # 帮助提示信息
        widgets = None  # 自定义插件
        error_messages = {
            'name': {'required': '用户名不能为空', },
            'age': {'required': '年龄不能为空', },
        }


def student(request):

    if request.method == 'GET':
        student_list = StudentList()
        return render(request, 'tests/test_finish.html', {'student_list': student_list})


