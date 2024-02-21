from .models import Transaction, Item
from rest_framework.serializers import ModelSerializer


class TransactionModelSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class ItemModelSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
