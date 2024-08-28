from django.db import models

class Invoice1(models.Model):
    num = models.IntegerField(default=0)
    value = models.FloatField(default=0)
    issue_date = models.CharField(max_length=10)
    parts_seller_name = models.CharField(max_length=30)
    parts_buyer_name = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    #pub_date = models.DateTimeField("date published")
    def __str__(self):
        return f"invoice #{self.num}"
