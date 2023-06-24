from typing import List

from django.db import IntegrityError
from django.shortcuts import get_object_or_404

from ninja import Router, Query
from ninja.pagination import paginate, LimitOffsetPagination

from base.filters import SearchNameFilterSchema
from base.schemas import ErrorSchema
from exercises.filters import ExerciseFilterSchema
from exercises.models import Exercise, Muscle, Equipment
from exercises.schemas import ExerciseSchema, MuscleSchema, EquipmentSchema, CreateExerciseSchema

router = Router()

@router.get("/exercises", response=List[ExerciseSchema])
@paginate(LimitOffsetPagination) 
def list_exercises(request, filters: ExerciseFilterSchema = Query(...)):
    queryset = Exercise.objects.all()
    exercises = filters.filter(queryset)
    return exercises

@router.get("/exercises/{id}", response=ExerciseSchema)
def get_exercise(request, id):
    exercise = get_object_or_404(Exercise, pk=id)
    return exercise

@router.post("/exercises", response={200: ExerciseSchema, 400: ErrorSchema})
def create_exercise(request, item: CreateExerciseSchema):
    target = get_object_or_404(Muscle, pk=item.target) if item.target is not None else None
    equipment,_ = Equipment.objects.get_or_create(name=item.equipment_name) if item.equipment_name is not None else None
    try:
        created_item = Exercise.objects.create(name=item.name, target=target, equipment=equipment, gif_url=item.gif_url)
        return created_item
    except IntegrityError:
        return 400, {"error": "Exercise with this name already exists"}


@router.get("/muscles", response=List[MuscleSchema])
def list_muscles(request, filters: SearchNameFilterSchema = Query(...)):
    queryset = Muscle.objects.all()
    muscles = filters.filter(queryset)
    return muscles

@router.get("/equipments", response=List[EquipmentSchema])
def list_equipments(request, filters: SearchNameFilterSchema = Query(...)):
    queryset = Equipment.objects.all()
    equipments = filters.filter(queryset)
    return equipments
