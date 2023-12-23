from typing import Optional

from ninja import FilterSchema, Field


class SearchNameFilterSchema(FilterSchema):
    search: Optional[str] = Field(q="name__icontains")
