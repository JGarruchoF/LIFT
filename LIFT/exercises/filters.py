from typing import Optional

from ninja import FilterSchema, Field

class ExerciseFilterSchema(FilterSchema):
    search: Optional[str] = Field(q=['name__icontains',
                                     'target__name__icontains',
                                     'equipment__name__icontains',
                                     ])
    target: Optional[int]

class SearchNameFilterSchema(FilterSchema):
    search: Optional[str] = Field(q='name__icontains')


