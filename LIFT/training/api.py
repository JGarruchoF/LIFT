from typing import List

from base.schemas import ErrorSchema
from django.shortcuts import get_object_or_404
from exercises.models import Exercise
from ninja import Query, Router
from ninja.pagination import LimitOffsetPagination, paginate
from ninja_jwt.authentication import JWTAuth

from training.filters import TrainingSessionFilterSchema
from training.models import ExerciseSession, Set, TrainingSession
from training.schemas import (
    ExerciseSessionSchema,
    ListTrainingSessionSchema,
    SetSchema,
    SetSchemaPatch,
    TrainingSessionSchema,
)

router = Router(auth=JWTAuth())


@router.get("/", response=List[ListTrainingSessionSchema])
@paginate(LimitOffsetPagination)
def list_trainings(request, filters: TrainingSessionFilterSchema = Query(...)):
    queryset = request.user.sessions
    trainings = filters.filter(queryset)
    return trainings.order_by("-created_at")


@router.get("/{id}", response=TrainingSessionSchema)
def get_training(request, id):
    queryset = request.user.sessions
    training = get_object_or_404(queryset, pk=id)
    return training


@router.post("/", response={200: TrainingSessionSchema, 400: ErrorSchema})
def create_training(request):
    user = request.user
    created_item = TrainingSession.objects.create(user=user)
    return created_item


@router.post("/{id}/add-exercise", response={200: ExerciseSessionSchema})
def add_exercise(request, id, exercise_id):
    training_session = get_object_or_404(request.user.sessions, pk=id)
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    new_session = ExerciseSession.objects.create(
        training_session=training_session, exercise=exercise
    )
    return new_session


@router.post("/{training_id}/{exercise_session_id}/add-set", response={200: SetSchema})
def add_set(request, training_id, exercise_session_id):
    exercise_session = get_object_or_404(
        ExerciseSession,
        training_session__user=request.user,
        training_session__id=training_id,
        pk=exercise_session_id,
    )
    new_set = Set.objects.create(exercise_session=exercise_session)

    return new_set


@router.patch(
    "/{training_id}/{exercise_session_id}/{set_id}",
    response={200: SetSchema, 403: ErrorSchema},
)
def update_set(
    request, training_id, exercise_session_id, set_id, set_data: SetSchemaPatch
):
    updated_set = get_object_or_404(
        Set.objects.prefetch_related("exercise_session__training_session__user"),
        pk=set_id,
        exercise_session=exercise_session_id,
        exercise_session__training_session=training_id,
        exercise_session__training_session__user=request.user,
    )
    for field, value in set_data.dict().items():
        setattr(updated_set, field, value)
    updated_set.save()

    return updated_set
