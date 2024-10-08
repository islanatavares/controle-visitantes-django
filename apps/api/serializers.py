from rest_framework import serializers
from porteiros.models import Porteiro
from usuarios.models import Usuario
from visitantes.models import Visitante

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
class PorteiroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Porteiro
        fields = '__all__'

class VisitanteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = '__all__'
