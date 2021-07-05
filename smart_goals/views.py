from rest_framework import generics
from .models import Goal
from .serializers import GoalSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly

class GoalList(generics.ListCreateAPIView):
    #queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Goal.objects.all().filter(owner = self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class GoalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer