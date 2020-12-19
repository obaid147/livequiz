from django.db import models

"""Our Questions and answers can be accessed using these variables (after views) from templates"""


class Quiz(models.Model):
    question_number = models.IntegerField(default=True)
    question = models.TextField(max_length=500, default=True)
    option1 = models.CharField(max_length=300)
    option2 = models.CharField(max_length=300)
    option3 = models.CharField(max_length=300)
    option4 = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
