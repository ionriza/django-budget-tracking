from django.db import models


# TODO: add 'icon'
#  (will be used to represent an icon for the category - food, transport, health
#  and we will use an icon library, i.e: bootstrap icons.
#  a text field is enough)
# TODO: add 'image'
#  (will be used to represent the logo/image of a vendor,
#  here we will use an imagefield and we will have to figure out
#  how to upload photos in Django)
class Expense(models.Model):
    amount = models.IntegerField()
    data = models.DateField()
    vendor = models.TextField()

    def __str__(self):
        return f'[{self.amount}]:{self.data} - {self.vendor}'