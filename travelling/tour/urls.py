from django.urls import path
from . import views

urlpatterns = [
    path('tour/', views.tour_view),
    path('', views.tour_view),
    path('tour_detail/<int:id>/', views.tour_detail_view),
    path('tour_list/', views.tour_delete_view),
    path('tour_list/<int:id>/delete/', views.tour_drop_view),
    path('create_post_tour/', views.createTourPostView),
    path('add-cooment/', views.createTourView),
]
