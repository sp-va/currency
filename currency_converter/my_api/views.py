from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CurrencySerializer
from .utils import get_currency

class RatesAPIView(APIView):
    def get(self, request):
        serializer = CurrencySerializer(data=request.query_params)
        if serializer.is_valid(raise_exception=True):
            from_currency = serializer.validated_data['from_currency']
            to_currency = serializer.validated_data['to_currency']
            value = serializer.validated_data['value']

            result = float(get_currency(from_currency=from_currency, to_currency=to_currency))
            final = result * float(value)

            return Response(final)


