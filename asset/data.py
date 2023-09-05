from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

from django.db.models import Q


from .models import User, Department, Station, Section
from .serializer import UserSerializer,StaffSerializer, DepartmentSerializer, SectionSerializer, StationSerializer, AssetSerializer, DeployedAssetSerializer

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

