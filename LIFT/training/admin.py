from django.contrib import admin

from training.models import TrainingSession, ExerciseSession, Set


@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    pass

@admin.register(ExerciseSession)
class ExerciseSessionAdmin(admin.ModelAdmin):
    pass

@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    pass
