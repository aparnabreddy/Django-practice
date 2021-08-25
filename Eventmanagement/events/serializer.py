from rest_framework import serializers
from events.models import event

class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model=event
        fields=('event_title','event_desc','venue','event_date')