from django.shortcuts import render
from .models import Transaction
from .serializers import TransactionModelSerializer
from rest_framework.generics import ListCreateAPIView
# Create your views here.

class TransactionListCreateView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionModelSerializer
