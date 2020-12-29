from django.contrib import admin
from .models import AdvancedQuiz


class AdvancedQuizAdmin(admin.ModelAdmin):
    list_display = ('question',)


admin.site.register(AdvancedQuiz, AdvancedQuizAdmin)
