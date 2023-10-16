from django.urls import path
from . import views

urlpatterns = [
    path('tour/', views.tour_view),
    path('', views.tour_view),
    path('tour_detail/<int:id>/', views.tour_detail_view),
    path('add-cooment/', views.createTourView),
]
