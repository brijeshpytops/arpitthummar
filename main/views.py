from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializers


@api_view(['GET', 'POST'])
def EmployeeListAPI(request):
    if request.method == 'GET':
        querySet = Employee.objects.all()
        serializers = EmployeeSerializers(querySet, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializers = EmployeeSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def EmployeeDetailAPI(request, employee_id):
    try:
        querySet = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return Response({'message': "Employee doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = EmployeeSerializers(querySet)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializers = EmployeeSerializers(querySet, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        serializers = EmployeeSerializers(querySet, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        querySet.delete()
        return Response({'message':"Employee is deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    