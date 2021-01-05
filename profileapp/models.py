from django.db import models


class Profile(models.Model):
    profile_pic = models.ImageField(default="prophoto.png", blank=True, null=True)
    # bio = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.profile_pic.url
