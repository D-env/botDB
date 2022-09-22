from rest_framework.serializers import ModelSerializer
from .models import Member, Event


class MemberSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Member

class EventSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Event

