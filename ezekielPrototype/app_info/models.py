from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45, default="")
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    join_date = models.DateTimeField(default=timezone.now)
    profile_picture = models.ImageField(default="")
    banner_picture = models.ImageField(default="")

    def __str__(self):
        return '%s, %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['first_name']
