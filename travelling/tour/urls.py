from django.urls import path
from . import views

urlpatterns = [
    path('tour/', views.TourView.as_view()),
    path('', views.TourView.as_view()),
    path('tour_detail/<int:id>/', views.TourDetailView.as_view()),
    path('create_post_tour/', views.CreateTourPostView.as_view()),
    path('tour_list/<int:id>/delete/', views.DropTourView.as_view()),
    path('tour_list/<int:id>/update/', views.UpdateTourPostView.as_view()),
    path('seacrh/', views.SearchTourView.as_view(), name='search'),
    path('add-cooment/', views.createTourView),
]
