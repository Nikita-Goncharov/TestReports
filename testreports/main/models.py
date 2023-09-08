from django.db import models
from django.contrib.auth.models import User


class Profile(User):
    # username
    # email
    date_of_birth = models.DateField()
    city = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.username} - {self.city}"
