from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('region-state/', views.RegionStateList.as_view(), name="region_state_list"),
    path('region-state/<int:pk>/', views.RegionStateDetail.as_view(), name="region_state_detail"),
    path('region-state/<int:pk>/schools/new/', views.SchoolCreate.as_view(), name="school_create"),
    path('region-state/<int:pk>/schools/<int:show_pk>/', views.SchoolDetail.as_view(), name="school_detail/")
]