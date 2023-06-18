from .serializers import (
    DepartmentSerializer, 
    PersonnelSerializer,
    DepartmentPersonnelSerializer
)
from .models import Department, Personnel
from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Department Listelemek için (Herkes);
class DepartmentListCreateView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (
        IsAuthenticated,
        IsAdminOrReadOnly,
    )

# Department Retriew, Update, Delete için (admin);
class DepartmentRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAuthenticated)
    
    def put(self, request, *args, **kwargs):
        if self.request.is_superuser or self.request.user.is_staff:
            return self.update(request, *args, **kwargs)
        data = {
            'message': 'You are not authorized to update!'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.is_superuser:
            # self.perform_destroy(instance)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        data = {
            'message': 'You are not authorized to update!'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)

    
        
# Personnel Listelemek için (Herkes);
class PersonnelListCreateView(ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = (
        IsAuthenticated,
        IsAdminOrReadOnly,
    )


# Personnel Retriew, Update, Delete için (admin);
class PersonnelRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = (IsAuthenticated)
    
    def put(self, request, *args, **kwargs):
        if self.request.is_superuser or self.request.user.is_staff:
            return self.update(request, *args, **kwargs)
        data = {
            'message': 'You are not authorized to update!'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.is_superuser:
            # self.perform_destroy(instance)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        data = {
            'message': 'You are not authorized to update!'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)


    
class DepartmentPersonnelView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentPersonnelSerializer
    permission_classes = (
        IsAuthenticated,
        IsAdminOrReadOnly,
    )

    def get_queryset(self):
        """
        Optionally restricts the returned department to a given one,
        by filtering against a `department` query parameter in the URL.
        """
        department = self.kwargs['department']
        if department is not None:
            return Department.objects.filter(name__iexact=department)
