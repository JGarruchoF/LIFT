from django.db import models

class Muscle(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=50, unique=True)
    target = models.ForeignKey(Muscle, null=True, on_delete=models.SET_NULL)
    equipment = models.ForeignKey(Equipment, null=True, on_delete=models.SET_NULL)
    gif_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


