from rest_framework import serializers

class BMRRequestSerializer(serializers.Serializer):
    weight = serializers.FloatField(required=False)
    height = serializers.FloatField(required=False)
    age = serializers.IntegerField(required=False)
    sex = serializers.ChoiceField(choices=["male", "female"], required=False)
    stress_factor = serializers.FloatField(required=False)
    activity_factor = serializers.FloatField(required=False)
    lean_body_mass = serializers.FloatField(required=False)
    ffm = serializers.FloatField(required=False)
    pa = serializers.FloatField(required=False)
    bsa = serializers.FloatField(required=False)


