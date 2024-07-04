from django.urls import path, include
from rest_framework_routers import DefaultRouter
from .views import PeliculaViewSet

router=DefaultRouter()
router.register('', PeliculaViewSet, basename="Pelicula")
urlpatterns = [
    path('', include(router.urls)) # Rutas generadas automaticamente
]
