from django.urls import path
from . import views

urlpatterns = [
    path(
        "work/", views.TransactionListCreateView.as_view(), name="work"
    ),  # For taking a look at all the transactions and also for sending posts to the database.
    path(
        "items/", views.ItemListView.as_view(), name="items"
    ),  # For taking a look at the current state of the database.
    path("", views.index, name="index"),
    path("verify/<str:rfid>/", views.verify, name="verify"),
    path("transactions/", views.transaction),
]
