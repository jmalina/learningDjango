from django.contrib.auth.models import User

from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from restcalc.models import Calculation
from restcalc.permissions import IsOwnerOrReadOnly
from restcalc.serializers import CalculationSerializer
from restcalc.serializers import UserSerializer


class CalculationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    