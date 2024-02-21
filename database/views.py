from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import serializers
from .models import Transaction, Item
from .serializers import TransactionModelSerializer, ItemModelSerializer
from rest_framework.response import Response
from rest_framework import status


class TransactionListCreateView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionModelSerializer

    def perform_create(self, serializer):
        request_data = self.request.data
        item_id = int(request_data.get('Item_Retrieved'))
        request_amount = int(request_data.get('Number_of_Items'))

        try:
            tracker(item_id=item_id, request_amount=request_amount)
        except serializers.ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemModelSerializer


def tracker(item_id, request_amount):
    item = Item.objects.get(id=item_id)

    if request_amount > item.remaining_number:
        raise serializers.ValidationError(
            "Request amount exceeds remaining number")

    item.remaining_number -= request_amount
    item.save()
