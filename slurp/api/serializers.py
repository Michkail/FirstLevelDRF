from rest_framework import serializers
from slurp.models import SlurpOffer

class SlurpOfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = SlurpOffer
        fields = "__all__"