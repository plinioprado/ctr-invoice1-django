from django.db import models

def get_active():
    return {i: i for i in {"Open": "open", "Paid": "paid", "Canceled": "canceled"}}

class Invoice1(models.Model):
    num = models.AutoField(primary_key=True)
    value = models.FloatField(default=0)
    issue_date = models.DateField("issue date")
    parts_seller_name = models.CharField(max_length=30)
    parts_buyer_name = models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=get_active, default="open")



    def __str__(self):
        return f"invoice #{self.num}"
