from rest_framework import serializers
from .models import PlatformModelCode


# 定义序列化类，需继承serializers.Serializer
class PlatformModelCodeSerializer(serializers.Serializer):
    # 将需要校验和序列化的字段加进来，变量名和字段类型需要和models.py中一致
    # 默认定义哪些字段，那么哪些字段就会序列化输出，同时这些字段也必须输入（传递）
    # name = serializers.CharField()
    # leader = serializers.CharField()

    class Meta:
        model = PlatformModelCode
        fields = '__all__'
