from myproject.models import Car
from rest_framework import routers, serializers, viewsets

class CarSerializer(serializers.ModelSerializer):

    class Meta: #declare attribute in class
        model = Car
        fields = ('model', 'detail', 'price', 'image')

class CarViewSet(viewsets.ModelViewSet): #view
    queryset = Car.objects.all()
    serializer_class = CarSerializer

router = routers.DefaultRouter()
router.register(r'car', CarViewSet)

