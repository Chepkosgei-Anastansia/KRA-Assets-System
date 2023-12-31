from rest_framework import serializers
from .models import User, Station, Department, Section, Asset, AssetsDeployed,DeployedAsset, Staff,Grade, Division

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AssetsDeployedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsDeployed
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields ="__all__"

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields ="__all__"

class DeployedAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeployedAsset
        fields ="__all__"