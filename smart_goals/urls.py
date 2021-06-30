from django.urls import base, path
from rest_framework import urlpatterns
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, GoalViewSet, NotesViewSet

router = DefaultRouter

router.register(r'user', UserViewSet, basename='user')
router.register(r'goal', GoalViewSet, basename='goal')
router.register(r'notes', NotesViewSet, basename='notes')

urlpatterns = router.urls
