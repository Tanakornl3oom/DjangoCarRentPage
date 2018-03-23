from myproject.models import Car,Rent,Person
from rest_framework import routers, serializers, viewsets

class CarSerializer(serializers.ModelSerializer):

    class Meta: #declare attribute in class
        model = Car
        fields = ('model', 'detail', 'price', 'image')

class CarViewSet(viewsets.ModelViewSet): #view
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class RentSerializer(serializers.ModelSerializer):

	class Meta: #declare attribute in class
	    model = Rent
	    fields = ('user', 'car', 'start_datetime', 'stop_datetime','fee')

class RentViewSet(viewsets.ModelViewSet): #view
	queryset = Rent.objects.all()
	serializer_class = RentSerializer

class PersonSerializer(serializers.ModelSerializer):

	class Meta: #declare attribute in class
	    model = Person
	    fields = ('first_name', 'last_name', 'telephone', 'dob','credit_amount','memo')

class PersonViewSet(viewsets.ModelViewSet): #view
	queryset = Person.objects.all()
	serializer_class = PersonSerializer

router = routers.DefaultRouter()
router.register(r'car', CarViewSet)
router.register(r'rent', RentViewSet)
router.register(r'person', PersonViewSet)



