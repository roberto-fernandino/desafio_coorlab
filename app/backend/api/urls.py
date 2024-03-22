from django.urls import path, include
from rest_framework import routers, viewsets
from .models import Trip, City
from .serializers import TripSerializer, CitiesSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView


router = routers.DefaultRouter()


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class CitiesViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitiesSerializer


class GetTripByCityId(ListAPIView):
    serializer_class = TripSerializer
    

    def get_queryset(self):
        city_id = self.kwargs.get('city_id')
        return Trip.objects.filter(city_id=city_id)


router.register(r"cities", CitiesViewSet, basename="city")
router.register(r"trips", TripViewSet, basename="trip")


urlpatterns = [
    path("", include(router.urls)),
    path("trips/by_city/<int:city_id>", GetTripByCityId.as_view())
]
