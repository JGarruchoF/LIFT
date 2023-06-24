from django.db import models

from base.models import TimeStampedModel
from users.models import User
from exercises.models import Exercise

class TrainingSession(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sessions")
    finished = models.BooleanField(default=False)
    duration = models.DurationField(null=True)


class ExerciseSession(TimeStampedModel):
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE, null=False)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=False)
    

class Set(models.Model):
    exercise_session = models.ForeignKey(ExerciseSession, on_delete=models.CASCADE, related_name='sets')
    weight = models.FloatField()
    reps = models.IntegerField()
    done = models.BooleanField(default=False)
    failure = models.BooleanField(default=False)
    warm_up = models.BooleanField(default=False)



