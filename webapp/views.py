from .serializers import myModelSerializer
from .models import myModel
from rest_framework import viewsets

class myModelList(viewsets.ModelViewSet):
    queryset = myModel.objects.all()
    serializer_class = myModelSerializer
    
    # you can write your own function here to override the default functions