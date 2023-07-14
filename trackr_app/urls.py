from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('region-state/', views.RegionStateList.as_view(), name="region_state_list"),
    path('region-state/<int:pk>/', views.RegionStateDetail.as_view(), name="region_state_detail"),
    path('region-state/<int:pk>/schools/new/', views.SchoolCreate.as_view(), name="school_create"),
    path('schools/<int:pk>/', views.SchoolDetail.as_view(), name="school_detail"),
    path('schools/<int:pk>/update/', views.SchoolUpdate.as_view(), name="school_update"),
    path('schools/<int:pk>/delete', views.SchoolDelete.as_view(), name="school_delete"),
]