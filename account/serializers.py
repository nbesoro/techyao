from rest_framework import serializers
from account.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    presentation =serializers.SerializerMethodField()
    date_joined = serializers.DateTimeField(format="%d/%m/%Y %H:%M", read_only=True)
    class Meta:
        model = Customer
        fields = [
            "id",
            "presentation",
            "date_joined",
            "first_name",
            "last_name",
            "email",
            "phone",
            "phone2",
            "addresse",
            "postal_code",
            "city",
            "gender",
        ]
        
    def get_presentation(self, obj):
        return f"{obj.gender}. {obj.get_full_name()}"
    
    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must be numeric.")
        if len(value) < 6:
            raise serializers.ValidationError("Phone number must be at least 6 digits.")
        return value

    def validate_phone2(self, value):
        if value and not value.isdigit():
            raise serializers.ValidationError("Phone2 must be numeric.")
        if value and len(value) < 6:
            raise serializers.ValidationError("Phone2 must be at least 6 digits.")
        return value

    def validate_postal_code(self, value):
        if len(value) != 5 or not value.isdigit():
            raise serializers.ValidationError("Postal code must be exactly 5 digits.")
        return value
