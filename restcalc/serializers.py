from rest_framework import serializers
from restcalc.models import Calculation
from django.contrib.auth.models import User

class CalculationSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Calculation
        fields = ('url', 'owner', 'name', 'calculation', 'value')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    calculation = serializers.HyperlinkedRelatedField(many=True, view_name='calculation-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'calculation')
