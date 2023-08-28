from django.shortcuts import render
from django.urls import reverse_lazy

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.db.models import Q


from .models import User, Department, Station, Section
from .serializer import UserSerializer, DepartmentSerializer, SectionSerializer, StationSerializer



class DepartmentList(APIView):
    def get(self, request, format=None):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentDetail(APIView):
    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        department= self.get_object(pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        department = self.get_object(pk)
        department.delete()
        return Response(satatus=status.HTTP_204_NO_CONTENT)
    

class StationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class StationRetreiveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer



class SectionList(APIView):
    def get(self, request, format=None):
        sections = Section.objects.all()
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SectionDetail(APIView):
    def get_object(self, pk):
        try:
            return Section.objects.get(pk=pk)
        except Section.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        section= self.get_object(pk)
        serializer = SectionSerializer(section)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        section = self.get_object(pk)
        serializer = SectionSerializer(section, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        section = self.get_object(pk)
        section.delete()
        return Response(satatus=status.HTTP_204_NO_CONTENT)
    

class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user= self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(satatus=status.HTTP_204_NO_CONTENT)
    
# def search_user(request):
#     if request.method =='POST':
#         search_query = request.POST['search_query']
#         user = User.objects.filter(personal_number_contains=search_query)
#         return Response(User)

class UserSearchView(generics.ListAPIView):
    serializer_class= UserSerializer
    
    def get_queryset(self):
        users = User.objects.all()
        serializer= UserSerializer(users)
        query = self.request.query_params.get('q')

        if query:
            users = users.filter(
                Q(personal_number__icontains=query) |
                Q(domain__icontains=query) |
                Q(role__icontains=query) |
                Q(name__icontains=query)
            )
        
            # return Response(serializer.users)
            return users
        
        return Response(satatus=status.HTTP_204_NO_CONTENT)
    

class StationSearchView(generics.ListAPIView):
    serializer_class= StationSerializer
    
    def get_queryset(self):
        stations = Station.objects.all()
        # serializer= StationSerializer(stations)
        query = self.request.query_params.get('q')

        if query:
            stations = stations.filter(
                Q(name__icontains=query)
            )
        
            
            return stations
        
        return Response(satatus=status.HTTP_204_NO_CONTENT)
    
class SectionSearchView(generics.ListAPIView):
    serializer_class= SectionSerializer
    
    def get_queryset(self):
        sections = Section.objects.all()
        # serializer= StationSerializer(stations)
        query = self.request.query_params.get('q')

        if query:
            sections = sections.filter(
                Q(name__icontains=query)
            )
            return sections
        
        return Response(satatus=status.HTTP_204_NO_CONTENT)
    

class DepartmentSearchView(generics.ListAPIView):
    serializer_class= DepartmentSerializer
    
    def get_queryset(self):
        departments = Department.objects.all()
        # serializer= StationSerializer(stations)
        query = self.request.query_params.get('q')

        if query:
            departments = departments.filter(
                Q(name__icontains=query)
            )
            return departments
        
        return Response(satatus=status.HTTP_204_NO_CONTENT)


        
