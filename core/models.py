from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Mentor(models.Model):
    name = models.CharField(max_length=30)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name
