from django.db import models
from django.contrib.auth.models import User
from checkout.models import BaseOrderInfo

# Create your models here.
class UserProfile(BaseOrderInfo):
    user = models.OneToOneField(User, related_name="profile_user")

    def __str__(self):
        return 'User Profile for: ' + self.user.username