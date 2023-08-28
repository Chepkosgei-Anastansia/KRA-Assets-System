from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .data import StaffModelUploadView
from .views import DepartmentDetail, DepartmentList, UserSearchView,DepartmentSearchView,StationSearchView,SectionSearchView, StationListCreateAPIView, StationRetreiveUpdateDestroyAPIView, SectionList, SectionDetail, UserList, UserDetail

urlpatterns = [
    path('department/', DepartmentList.as_view(), name='department-list-create'),
    path('department/<int:pk>/', DepartmentDetail.as_view(), name='department-retrieve-update-destroy'),
    
    path('station/', StationListCreateAPIView.as_view(), name='station-list-create'),
    path('station/<int:pk>/', StationRetreiveUpdateDestroyAPIView.as_view(), name='station-retrieve-update-destroy'),

    path('section/', SectionList.as_view(), name='section-list-create'),
    path('section/<int:pk>/', SectionDetail.as_view(), name='section-retrieve-update-destroy'),

    path('user/', UserList.as_view(), name='user-list-create'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user-retrieve-update-destroy'),

    path('user_search/', UserSearchView.as_view(), name='user-search'),
    path('department_search/', DepartmentSearchView.as_view(), name='department-search'),
    path('section_search/',SectionSearchView.as_view(), name='section-search'),
    path('station_search/', StationSearchView.as_view(), name='station-search'),

    path('upload/staff_model/', StaffModelUploadView.as_view(), name='upload_staff'),
]

urlpatterns = format_suffix_patterns(urlpatterns)