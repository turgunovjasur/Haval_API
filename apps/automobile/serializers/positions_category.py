from rest_framework import serializers

from automobile.models.position_category import PositionCategory


class PositionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionCategory
        fields = "__all__"


class ComparePositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionCategory
        fields = [
            "lockingRearWheelDifferential",
            "automaticAutoHold",
            "childSeatLock",
            "led_headlight",
            "full_weight",
            "transmission_box",
            "seats_count",
            "max_speed",
        ]
