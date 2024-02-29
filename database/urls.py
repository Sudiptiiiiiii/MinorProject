from django.urls import path
from . import views
urlpatterns = [
    path('transaction/', views.TransactionListCreateView.as_view(),
         name="transactions"), # For taking a look at all the transactions and also for sending posts to the database.
    path('items/', views.ItemListView.as_view(), name='items'), # For taking a look at the current state of the database.
    path('', views.index, name='index')
]
