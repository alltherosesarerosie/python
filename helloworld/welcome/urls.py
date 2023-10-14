from django.urls import path
from . import views

urlpatterns = [
    path('', views.pr_lan_view),
    path('lang_detail/<int:id>/', views.pr_lan_detail_view)
]