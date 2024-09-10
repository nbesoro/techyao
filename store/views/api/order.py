from django.urls import reverse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from store.models import Order
from store.serializers import OrderSerializer, OrderPdfSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    search_fields = ["number", "customer__first_name", "customer__last_name"]

    def get_serializer_class(self):
        if self.action == "list":
            return OrderPdfSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        order_id = response.data["id"]
        url = request.build_absolute_uri(
            reverse("generate_invoice_pdf", kwargs={"order_id": order_id})
        )
        custom_response = {
            "pdf_url": url,
            "order": response.data,  # Les données de l'objet créé
            "status_code": status.HTTP_201_CREATED,
        }

        return Response(custom_response, status=status.HTTP_201_CREATED)

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
