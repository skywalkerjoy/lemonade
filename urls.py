from django.urls import path
from . import views

urlpatterns = [
  path('',views.home, name ='home'),
  path('<int:menu_id>/detail/',views.detail,name='detail'),
  
]
