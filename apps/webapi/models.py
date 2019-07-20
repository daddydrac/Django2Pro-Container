from django.db import models

# Create your models here.

class Navigation(models.Model):

    # Python Constants for Enums
    admin = "admin"
    user = "user"


    # Enumerations
    type_choice = (
        (admin, "admin"),
        (user, "user")
    )
    type = models.CharField(
        max_length=8,
        choices=type_choice,
        default=user
    )
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    uri = models.CharField(max_length=200)

    def __str__(self):
        return self.name

