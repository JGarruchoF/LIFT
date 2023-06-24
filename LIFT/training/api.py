from typing import List

from django.shortcuts import get_object_or_404

from ninja import Router, Query
from ninja.pagination import paginate, LimitOffsetPagination

from base.schemas import ErrorSchema
from training.filters import TrainingSessionFilterSchema
from training.models import TrainingSession
from training.schemas import TrainingSessionSchema, CreateTrainingSessionSchema

router = Router()

@router.get("/", response=List[TrainingSessionSchema])
@paginate(LimitOffsetPagination) 
def list_trainings(request, filters: TrainingSessionFilterSchema = Query(...)):
   queryset = request.user.sessions
   trainings = filters.filter(queryset)
   return trainings

@router.get("/{id}", response=TrainingSessionSchema)
def get_training(request, id):
   queryset = request.user.sessions
   training = get_object_or_404(queryset, pk=id)
   return training

@router.post("/", response={200: TrainingSessionSchema, 400: ErrorSchema})
def create_training(request, item: CreateTrainingSessionSchema):
   user = request.user
   created_item = TrainingSession.objects.create(user=user)
   return created_item