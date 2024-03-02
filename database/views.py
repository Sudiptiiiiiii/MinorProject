from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import serializers
from .models import Transaction, Item, Cards
from .serializers import TransactionModelSerializer, ItemModelSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.core.exceptions import ObjectDoesNotExist
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class TransactionListCreateView(
    ListCreateAPIView
):  # For handling requests and transactions
    queryset = Transaction.objects.all()
    serializer_class = TransactionModelSerializer

    def perform_create(self, serializer):
        request_data = self.request.data
        item_id = int(request_data.get("Item_Retrieved"))
        request_amount = int(request_data.get("Number_of_Items"))

        try:
            tracker(
                item_id=item_id, request_amount=request_amount
            )  # This line calls the tracking function.
        except (
            serializers.ValidationError
        ) as e:  # In case the number of requested items is higher than the available items.
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()


class ItemListView(
    ListAPIView
):  # for listing the current status of the database with- Name of the items present, Number of the items present.
    queryset = Item.objects.all()
    serializer_class = ItemModelSerializer


def tracker(
    item_id, request_amount
):  # For updating the database according to the number of available items. - This function is called for tracking.
    item = Item.objects.get(id=item_id)

    if request_amount > item.remaining_number:
        raise serializers.ValidationError("Request amount exceeds remaining number")

    item.remaining_number -= (
        request_amount  # Updates the particulr data in the database.
    )
    item.save()  # Save the update to the database.


# -----------------------------------------------------------------------------------
def index(request):
    transactions = Transaction.objects.all()
    context = {"transactions": transactions}
    return render(request, "database/index.html", context)


def verify(request, rfid):
    try:
        item = Cards.objects.get(card_Number=rfid)
        data = {"status": "Verified"}
    except ObjectDoesNotExist:
        data = {"status": "Unverified"}

    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def transaction(request):
    print(request.body)
    request_data = request.body
    print(request_data)
    request_data_str = request_data.decode("utf-8")

    # Parse the string as JSON
    data = json.loads(request_data_str)
    item_id = data.get("Item_Retrieved")
    request_amount = data.get("Number_of_Items")
    card_number = data.get("Card_number")
    print(item_id)
    print(request_amount)
    print(card_number)

    if verify_card(card_number):
        try:
            item = Item.objects.get(id=item_id)
        except ObjectDoesNotExist:
            data = {"message": "no such items", "status": 500}
            json_data = json.dumps(data)
            return HttpResponse(json_data, content_type="application/json")

        no_of_remaining_item = item.remaining_number
        if request_amount > no_of_remaining_item:
            data = {"message": "Request Amount exceeds reamining Number", "status": 500}
            json_data = json.dumps(data)
            return HttpResponse(json_data, content_type="application/json")
        else:
            data = {"message": "Items Retriving", "status": 200}
            item.remaining_number = no_of_remaining_item - request_amount
            item.save()
            transaction = Transaction(
                card_Number=Cards.objects.get(card_number=card_number),
                Item_Retrieved=item,
                Number_of_Items=request_amount,
            )
            transaction.save()
            json_data = json.dumps(data)
            return HttpResponse(json_data, content_type="application/json")
    else:
        data = {"message": "no such card", "status": 500}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type="application/json")


def verify_card(rfid):
    try:
        card = Cards.objects.get(card_number=rfid)
        return True
    except ObjectDoesNotExist:
        return False
