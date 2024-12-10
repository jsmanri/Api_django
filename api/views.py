from rest_framework import viewsets
from .serializer import ProgrammerSerializer, studentSerializer
from .models import programmer , student


# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = ProgrammerSerializer
    
class studentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer