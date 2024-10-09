from django.urls import include, path
from rest_framework import routers

from api.viewsets import PorteiroViewSet, UsuarioViewSet, VisitanteViewSet

router = routers.DefaultRouter()

router.register(r'usuarios', UsuarioViewSet)
router.register(r'porteiros', PorteiroViewSet)
router.register(r'visitantes', VisitanteViewSet)

urlpatterns = [
    path('', include(router.urls)),
 
]

