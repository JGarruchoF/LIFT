from typing import Optional
import datetime

from ninja import FilterSchema


class TrainingSessionFilterSchema(FilterSchema):
    created_at: Optional[datetime.datetime]
