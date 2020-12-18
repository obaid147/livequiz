from django.contrib import admin
from .models import Quiz


""" Class QuizAdmin is used to show and use database properly and easily ie: the name QuizAdmin"""


class QuizAdmin(admin.ModelAdmin):
    list_display = ('question',)


# registering our models


admin.site.register(Quiz, QuizAdmin)
