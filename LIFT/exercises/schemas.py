from ninja import Schema, ModelSchema
from typing import Optional



from exercises.models import Muscle,Equipment,Exercise

class ErrorSchema(Schema):
    error: str

class MuscleSchema(ModelSchema):
    class Config:
        model = Muscle 
        model_fields = ['id', 'name']

class EquipmentSchema(ModelSchema):
    class Config:
        model = Equipment 
        model_fields = ['id', 'name']

class ExerciseSchema(ModelSchema):
    class Config:
        model = Exercise
        model_fields = ['id', 'name','target','equipment','gif_url']

class CreateExerciseSchema(ModelSchema):
    equipment_name: Optional[str] = None
    class Config:
        model = Exercise 
        model_fields = ['name','target','gif_url']

