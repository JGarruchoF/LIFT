from ninja import NinjaAPI

from exercises.api import router as exercises_router


api = NinjaAPI()

api.add_router("/", exercises_router)
