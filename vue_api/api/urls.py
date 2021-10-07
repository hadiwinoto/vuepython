from django.urls import path
from . import views

urlpatterns = [
    # path('',views.apiOverview, name='apiOverview'),
    path('list-mobil/',views.showAll, name='list-mobil'),
    path('detail-mobil/<int:pk>/',views.detailMobil, name='detail-mobil'),
    path('tambah-mobil/',views.createMobil, name='tambah-mobil'),
    path('edit-mobil/',views.createMobil, name='edit-mobil'),
    path('delete-mobil/<int:pk>/',views.createMobil, name='delete-mobil'),
]