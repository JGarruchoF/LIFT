from typing import List
import datetime

from ninja import ModelSchema

from training.models import TrainingSession, ExerciseSession, Set
from exercises.schemas import BasicExerciseSchema

class SetSchemaPatch(ModelSchema):
    class Config:
        model = Set
        model_fields = [
            'weight',
            'reps',
            'done',
            'failure',
            'warm_up',
            ]
        model_fields_optionals = '__all__'
class SetSchema(ModelSchema):
    class Config:
        model = Set
        model_fields = [
            'id',
            'exercise_session',
            'weight',
            'reps',
            'done',
            'failure',
            'warm_up',
            ]

class ExerciseSessionSchema(ModelSchema):
    sets: List[SetSchema]
    exercise: BasicExerciseSchema
    class Config:
        model = ExerciseSession
        model_fields = ['id']

class ListTrainingSessionSchema(ModelSchema):
    created_at: datetime.datetime
    updated_at: datetime.datetime
    class Config:
        model = TrainingSession
        model_fields = ['id', 'user', 'finished']

class TrainingSessionSchema(ModelSchema):
    exercise_sessions: List[ExerciseSessionSchema]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    class Config:
        model = TrainingSession
        model_fields = ['id', 'user', 'finished']
