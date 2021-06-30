from rest_framework import serializers
from .models import User, Goal, Notes

class UserSerializer(serializers.ModelSerializer):
    view_name = 'your_name',
    many = False,
    read_only = True

    class Meta:
        model = User
        fields = ('id', 'your_name', 'specific', 'measurable', 'achievable', 'relevant', 'timely')

class GoalSerializer(serializers.ModelSerializer):
    view_name = 'view_goals',
    many = True,
    read_only = True

    class Meta:
        model = Goal
        fields = ('overall_goal')

class NotesSerializer(serializers.ModelSerializer):
    view_name= 'notes'
    many = True,
    read_only = True

    class Meta: 
        model = Notes
        fields = ('notes')
