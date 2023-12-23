from exercises.api import router as exercises_router
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController
from training.api import router as training_router

api = NinjaExtraAPI()

# Adds routes 'token/pair', 'token/refresh' and 'token/verify'
api.register_controllers(NinjaJWTDefaultController)

api.add_router("/", exercises_router)
api.add_router("/trainings", training_router)

print("hola")
