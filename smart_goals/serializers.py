from rest_framework import serializers
from .models import Goal

class GoalSerializer(serializers.ModelSerializer):
    view_name = 'view_goals'

    class Meta:
        model = Goal
        fields = ('id', 'specific', 'measureable', 'achievable', 'relevant', 'timely', 'overall_goal', 'notes')
