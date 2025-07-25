from rest_framework import serializers
from .models import Policy, Claim

class PloicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'
        
        
class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = '__all__'
        