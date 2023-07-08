from typing import Optional
import datetime

from ninja import ModelSchema

from training.models import TrainingSession

class TrainingSessionSchema(ModelSchema):
    created_at: datetime.datetime
    updated_at: datetime.datetime
    class Config:
        model = TrainingSession
        model_fields = ['id', 'user', 'finished']


