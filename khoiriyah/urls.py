from django.urls import path
from . import views

urlpatterns = [
    path('', views.khoiriyah_detail, name='khoiriyah_detail'),
    path('add/<product_id>', views.khoiriyah_add, name='khoiriyah_add'),
    path('remove/<product_id>', views.khoiriyah_remove, name='khoiriyah_remove'),
]
