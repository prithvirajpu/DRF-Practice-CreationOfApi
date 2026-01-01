from django.urls import path
from . import views

urlpatterns=[
    path('get/',views.getUser),
    path('create/',views.create_user),
    path('update/<int:id>',views.update_user),
]
