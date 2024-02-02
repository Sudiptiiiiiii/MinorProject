from django.db import models

# Create your models here.
class Transaction(models.Model): 
    Card_Number = models.CharField(max_length = 256)
    Item_Retrieved = models.CharField(max_length = 256, blank=True, null=True)
    Number_of_Items = models.IntegerField(blank=True, null=True)
    Date_of_Transaction = models.DateField(auto_now_add = True)
    def __str__(self):
        return f"{self.Card_Number} ({self.Date_of_Transaction})"