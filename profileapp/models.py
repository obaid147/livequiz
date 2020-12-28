from django.db import models


class Profile(models.Model):
    profile_pic = models.ImageField(default="prophoto.png", blank=True, null=True)
    bio = models.TextField(max_length=500, null=True, blank=True, default=True)

    def __str__(self):
        return self.profile_pic.name