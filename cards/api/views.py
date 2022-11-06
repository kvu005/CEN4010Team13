from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from cards.api.serializers import BaseCreditCardSerializer


class CreditCardViewSet(viewsets.ViewSet):

    def create(self, request: Request) -> BaseCreditCardSerializer:
        serializer = BaseCreditCardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
