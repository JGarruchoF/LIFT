from django.db import models

from base.models import TimeStampedModel
from exercises.models import Exercise
from users.models import User

class TrainingSession(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sessions")
    finished = models.BooleanField(default=False)
    duration = models.DurationField(null=True)


class ExerciseSession(TimeStampedModel):
    training_session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE, related_name="exercise_sessions", null=False)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return f"{self.id}"

class Set(models.Model):
    exercise_session = models.ForeignKey(ExerciseSession, on_delete=models.CASCADE, related_name='sets')
    weight = models.FloatField(blank=True, null=True)
    reps = models.IntegerField(blank=True, null=True)
    done = models.BooleanField(default=False)
    failure = models.BooleanField(default=False)
    warm_up = models.BooleanField(default=False)

    def __str__(self):
        if self.done:
            return f"{self.exercise_session.exercise.name} ({self.weight} kg): {self.reps} reps"
        else: 
            return f"{self.exercise_session.exercise.name}: undone"



