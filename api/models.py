from django.db import models


# Create your models here.
class Member(models.Model):
    Id = models.AutoField(primary_key=True, null=False)
    Name = models.CharField(max_length=500, null=False)
    Membership = models.CharField(max_length=500, null=False)
    ExperianceType = models.CharField(max_length=500, null=False)
    Email = models.CharField(max_length=500, null=True)
    DateOfJoining = models.DateTimeField(auto_now_add=True, null=False)
    PhotoFile = models.ImageField(upload_to="members/profile_pictures/", null=True)
    KnownLanguages = models.JSONField(null=True)
    BooksWritten = models.JSONField(null=True)
    WorkingHours = models.JSONField(null=True)
    Projects = models.JSONField(null=True)
    About = models.TextField(max_length=5000, null=False)

    def __str__(self) -> str:
        return self.Name

