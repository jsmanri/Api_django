from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'Programmer', views.ProgrammerViewSet)
router.register(r'student', views.studentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]