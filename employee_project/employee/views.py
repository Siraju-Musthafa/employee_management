from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import employeetable
from .serializers import employeeserializers


@api_view(['POST'])
def add_employee(request):
    serializer = employeeserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_employeeby_id(request, id):
    try:
        employee = employeetable.objects.get(id=id)
    except employeetable.DoesNotExist:
        return Response(
            {'error': 'Employee not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = employeeserializers(employee)
    return Response(serializer.data)


@api_view(['GET'])
def get_active_employee(request):
    employees = employeetable.objects.filter(status='ACTIVE')
    serializer = employeeserializers(employees, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_employee(request, id):
    try:
        employee = employeetable.objects.get(id=id)
    except employeetable.DoesNotExist:
        return Response(
            {'error': "Employee not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = employeeserializers(
        employee,
        data=request.data,
        partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_employee(request, id):
    try:
        employee = employeetable.objects.get(id=id)
    except employeetable.DoesNotExist:
        return Response(
            {"error": "Employee not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    employee.status = 'INACTIVE'
    employee.save()
    return Response({"message": "Employee marked as INACTIVE"})
