from django.db import models

# Create your models here.
class Contact(models.Model):
    Sno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500, null=False)
    Email = models.CharField(max_length=500, null=False)
    Message = models.TextField(max_length=5000, null=False)
    DateSent = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self) -> str:
        return self.Email
