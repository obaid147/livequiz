from django.db import models

"""Our Questions and answers can be accessed using these variables (after views) from templates"""


class Quiz(models.Model):
    question_number = models.IntegerField(default=True)
    question = models.TextField(max_length=500, default=True)
    option1 = models.CharField(max_length=300, default=True)
    option2 = models.CharField(max_length=300, default=True)
    option3 = models.CharField(max_length=300, default=True)
    option4 = models.CharField(max_length=300, default=True)
    answer = models.CharField(max_length=300, default=True)


class Tasks(models.Model):
    title = models.CharField(max_length=200, default=None)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.title
