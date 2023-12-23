from django.contrib import admin

from exercises.models import Exercise, Muscle, Equipment


@admin.register(Muscle)
class ExerciseAdmin(admin.ModelAdmin):
    pass


@admin.register(Equipment)
class ExerciseAdmin(admin.ModelAdmin):
    pass


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass
