from django.db import models


class Item(models.Model): #For defining the items present in the vending machine. And keeping track of the items present there.
    Name = models.CharField(max_length=100)
    remaining_number = models.IntegerField()

    def __str__(self):
        return f'{self.Name} ({self.id})'


class Transaction(models.Model): # For keeping record of the transactions. 
    Card_Number = models.CharField(max_length=256)
    Item_Retrieved = models.ForeignKey(Item, on_delete=models.CASCADE)
    Number_of_Items = models.IntegerField(blank=True, null=True)
    Date_of_Transaction = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.Card_Number} ({self.Date_of_Transaction})"
