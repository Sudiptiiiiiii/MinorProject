from .models import Transaction, Item
from rest_framework.serializers import ModelSerializer


class TransactionModelSerializer(ModelSerializer): # For serializing the Transaction model into json format. 
    class Meta:
        model = Transaction
        fields = "__all__"


class ItemModelSerializer(ModelSerializer): # For serializing the Item model into json format.
    class Meta:
        model = Item
        fields = "__all__"
