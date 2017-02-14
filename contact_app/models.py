from django.db import models


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=130, blank=True, null=True)
    phone = models.CharField(max_length=130, blank=True, null=True)
    suite = models.CharField(max_length=130, blank=True, null=True)
    street = models.CharField(max_length=130, blank=True, null=True)
    city = models.CharField(max_length=130, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    zipcode = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        db_table = 'tblcontact'





