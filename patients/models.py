from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    dob = models.DateField()
    contact_number = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=10)
    relative_name = models.CharField(max_length=200)
    relative_address = models.CharField(max_length=200)
    reason_for_admission = models.TextField()
    
    def __str__(self):
        return self.name
