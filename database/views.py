from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import serializers
from .models import Transaction, Item
from .serializers import TransactionModelSerializer, ItemModelSerializer
from rest_framework.response import Response
from rest_framework import status


class TransactionListCreateView(ListCreateAPIView): #For handling requests and transactions
    queryset = Transaction.objects.all()
    serializer_class = TransactionModelSerializer

    def perform_create(self, serializer):
        request_data = self.request.data
        item_id = int(request_data.get('Item_Retrieved'))
        request_amount = int(request_data.get('Number_of_Items'))

        try:
            tracker(item_id=item_id, request_amount=request_amount) # This line calls the tracking function.
        except serializers.ValidationError as e: # In case the number of requested items is higher than the available items.
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()


class ItemListView(ListAPIView): #for listing the current status of the database with- Name of the items present, Number of the items present. 
    queryset = Item.objects.all()
    serializer_class = ItemModelSerializer


def tracker(item_id, request_amount): # For updating the database according to the number of available items. - This function is called for tracking.
    item = Item.objects.get(id=item_id)

    if request_amount > item.remaining_number:
        raise serializers.ValidationError(
            "Request amount exceeds remaining number")

    item.remaining_number -= request_amount # Updates the particulr data in the database. 
    item.save() # Save the update to the database.
