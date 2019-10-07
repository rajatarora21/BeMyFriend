from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('details',views.details,name='details'),
    path('passwordCheck',views.passwordCheck, name='passwordCheck')
]