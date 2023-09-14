from rest_framework import serializers

class CurrencySerializer(serializers.Serializer):
    from_currency = serializers.CharField()
    to_currency = serializers.CharField()
    value = serializers.DecimalField(max_digits=10, decimal_places=4)


