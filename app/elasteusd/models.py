from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organisation(models.Model):
    fullname = models.CharField(max_length=60)
    shortname = models.CharField(max_length=60)

    def add_user(self, user):
        link = UserOrganisation()
        link.user = user
        link.organisation = self
        link.save()

    def __str__(self):
        return self.fullname

class UserOrganisation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.get_full_name() + " at " + self.organisation.fullname