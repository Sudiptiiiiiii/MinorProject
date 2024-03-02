# MinorProject

Important End Points
-> /api/transactions/
-> /api/verify/<str:Card_number>

Database Structure
3 Models 
-> Cards
-> Items
-> Transaction -> has Foreign Key Relation with Cards and Items


Endpoint Description
-> /api/transactions/

Most important Endpoint. When data is send to the this end point from the NodeMCU
In the following format.
{   "Card_number": "abcdef",  (needs to be string)  
    "Number_of_Items":10000,  (needs to be integer)
    "Item_Retrieved": 1       (needs to be integer)
}

Card_number is checked by server from the Cards table i.e. if the card is in database it will be verified or else it wont be verified.
Number_of_Items is the number of the items that user wants to receive. It will be verified first if the amoint is available then only the transaction will be proceeded.
Item_Retrived is the id of the items that is going to be retrived.

In above JSON data 
if the card_number "abcdef" is in the database and number of items of item_retrived (id = 1, lets say i.e. paper) is equal to or less than required than only item will be dispensed.