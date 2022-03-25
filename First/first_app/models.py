from django.db import models

# Create your models here.

class Question(models.Model):
    text     = models.CharField(max_length=300)
    pub_data = models.DateField()

    def __str__(self):
        return self.text


class Choice(models.Model):
    text     = models.CharField(max_length=300)
    vote     = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text