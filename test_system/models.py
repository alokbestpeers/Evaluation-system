from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    technology = models.ManyToManyField(Technology, related_name='skills')

    def __str__(self):
        return self.name


class Questions(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    technology = models.ManyToManyField(Technology, related_name='technology')

    def __str__(self):
        return self.question
