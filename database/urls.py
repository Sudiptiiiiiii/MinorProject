from django.urls import path
from . import views
urlpatterns = [
    path('transaction/', views.TransactionListCreateView.as_view(),
         name="transactions"),
    path('items/', views.ItemListView.as_view(), name='items'),
    path('update/<int:item_id>/',
         views.tracker, name="updateDb")
]
