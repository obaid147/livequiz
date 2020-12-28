from django.db import models


class Profile(models.Model):
    profile_pic = models.ImageField(blank=True, null=True, default=True)
    bio = models.TextField(max_length=500, null=True, blank=True, default=True)

    def __str__(self):
        return self.profile_pic.name
