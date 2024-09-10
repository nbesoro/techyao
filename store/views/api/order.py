from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from store.models import Order
from store.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=["post"])
    def validate(self, request):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            return Response(
                {
                    "message": "Data is valid, but not saved.",
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
