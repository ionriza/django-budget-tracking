from django.db import models


class Category(models.Model):
    name = models.TextField()
    icon = models.TextField()

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name


class Expense(models.Model):
    amount = models.IntegerField()
    data = models.DateField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.data}]:{self.amount}"
