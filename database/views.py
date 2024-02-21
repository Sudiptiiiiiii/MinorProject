from django.shortcuts import render
from .models import Transaction, Item
from .serializers import TransactionModelSerializer
from rest_framework.generics import ListCreateAPIView
# Create your views here.


class TransactionListCreateView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionModelSerializer

    def perform_create(self, serializer):
        request_data = self.request.data
        tracker(item_id=int(request_data.get('Item_Retrieved')),
                request_amount=int(request_data.get('Number_of_Items')))
        serializer.save()


def tracker(item_id, request_amount):
    item = Item.objects.get(id=item_id)
    item.remaining_number -= request_amount
    item.save()
