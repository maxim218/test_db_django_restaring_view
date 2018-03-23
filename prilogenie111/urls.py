from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add_records/', views.add_records, name='add_records'),
    url(r'^delete_all_records/', views.delete_all_records, name='delete_all_records'),
]