from django.db import models


class Students(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    emailaddress = models.EmailField(max_length=30)
    DOB = models.DateField()
    age = models.IntegerField()
    class Meta:
        db_table = 'students'
