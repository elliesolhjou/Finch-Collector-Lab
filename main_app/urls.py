from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>', views.finches_detail, name='detail'),
    path('finch/create/', views.CreateFinch.as_view(), name='finch_create'),
    path('finch/<int:pk>/update/', views.CreateFinch.as_view(), name='finch_update'),
    path('finch/<int:pk>/delete/', views.DeleteFinch.as_view(), name='finch_delete'),
]