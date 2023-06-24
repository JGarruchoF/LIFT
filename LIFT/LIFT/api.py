from ninja import NinjaAPI

from exercises.api import router as exercises_router
from training.api import router as training_router


api = NinjaAPI()

api.add_router("/", exercises_router)
api.add_router("/training", training_router)
