from django.shortcuts import render
from django.http import JsonResponse
from teachers.models import Teacher
from .serializers import TeacherSerializer,StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from student.models import Student
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics  

# Create your views here.
@api_view(['GET', 'POST'])
def teachers_api_view(request):
    if request.method == "GET":
        teachers = Teacher.objects.all()
        serialized_data = TeacherSerializer(teachers, many=True)
        return Response(serialized_data.data, 
                        status=status.HTTP_200_OK)
    elif request.method == "POST":
        query_set = TeacherSerializer(data=request.data)
        if query_set.is_valid():
            query_set.save() # Save the data into DB
            return Response(query_set.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(query_set.errors, 
                            status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE '])
def teacher_detail(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == "GET":
        serialized_data = TeacherSerializer(teacher)
        return Response(serialized_data.data,
                        status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = request.data
        serial = TeacherSerializer(teacher, 
                                   data=data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_200_OK)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
#@api_view(['GET'])
class StudentView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)     

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)
        else:
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
'''
'''
# Mixins
class StudentView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()    # Queryset is required for ListModelMixin
    serializer_class = StudentSerializer    # Serializer class is required for CreateModelMixin

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
    
class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()    
    serializer_class = StudentSerializer    

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
'''

# Generic Views
class StudentView(generics.ListAPIView, generics.ListCreateAPIView):
    queryset = Student.objects.all()    
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()    
    serializer_class = StudentSerializer

