from django.urls import path
from . import views
urlpatterns = [
    path('transaction/', views.TransactionListCreateView.as_view(),
         name="transactions"),
    path('update/<int:item_id>/',
         views.tracker, name="updateDb")
]
