from django.contrib import admin
from .models import IntermediateQuiz




class IntermediateQuizAdmin(admin.ModelAdmin):
    list_display = ('question',)



admin.site.register(IntermediateQuiz, IntermediateQuizAdmin)