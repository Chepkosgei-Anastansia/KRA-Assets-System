from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

from django.db.models import Q


from .models import User, Department, Station, Section, Division, Grade, Staff
from .serializer import UserSerializer,StaffSerializer, DepartmentSerializer, SectionSerializer, StationSerializer, AssetSerializer, DeployedAssetSerializer, DivisionSerializer,GradeSerializer

class ExcelToDBUploadView(APIView):
    serializer_class = None

    def post(self, request, format=None):
        if 'excel_file' not in request.FILES:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        excel_file = request.FILES['excel_file']
        data = pd.read_excel(excel_file)


        for index,row in data.iterrows():
            serializer = self.serializer_class(data=row)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message:''Data uploaded successfully'}, status=status.HTTP_201_CREATED)
                

        return Response({'Message:''Data Not uploaded successfully'}, status=status.HTTP_201_CREATED)
        
class StaffTestExcelUploadView(APIView):
    def post(self, request, format=None):
        if 'excel_file' not in request.FILES:
            return Response({'error': 'No file provided. Uploan an Excel File'}, status=status.HTTP_400_BAD_REQUEST)

        excel_file = request.FILES['excel_file']
        excel_data = pd.read_excel(excel_file)

        for index, row in excel_data.iterrows():
            
                staff_number = row['Staff Number']
                staff_name = row['Staff Name']
                designation = row['Designation']
                grade = row['Designation']
                department = row['Department']
                division = row['Division']
                section = row['Section']
                station = row['Station']

                # Create or retreive department
                department, created = Department.objects.get_or_create(name=department)
                department_serializer=DepartmentSerializer(department)

                division, created = Division.objects.get_or_create(name=division, department=department)
                division_serializer = DivisionSerializer(division)

                section, created = Section.objects.get_or_create(name=section, division=division)
                section_serializer = SectionSerializer(section)

                # Create or retreive station
                station, created = Station.objects.get_or_create(name=station)
                station_serializer=StationSerializer(station)

                 # Create or retreive grade
                grade, created = Grade.objects.get_or_create(designation=grade)
                grade_serializer=GradeSerializer(grade)

                # handling  duplicate staff entries

                existing_staff = Staff.objects.filter(staff_number=staff_number)
                if existing_staff:
                    continue

                staff = Staff.objects.create(
                    staff_number= staff_number,
                    staff_name=staff_name,
                    grade=grade,
                    department= department,
                    division =division,
                    section =section,
                    station = station
                )
                staff_serializer=StaffSerializer(staff)
        return Response({'message': 'Data uploaded successfully'}, status=status.HTTP_201_CREATED)



class StaffModelUploadView(ExcelToDBUploadView):
    serializer_class=StaffSerializer

class DepartmentUploadView(ExcelToDBUploadView):
    serializer_class=DepartmentSerializer

class StationUploadView(ExcelToDBUploadView):
    serializer_class=StationSerializer

class SectionModelUploadView(ExcelToDBUploadView):
    serializer_class=SectionSerializer

class AssetModelUploadView(ExcelToDBUploadView):
    serializer_class=AssetSerializer

class DeployedAssetModelUploadView(ExcelToDBUploadView):
    serializer_class=DeployedAssetSerializer

