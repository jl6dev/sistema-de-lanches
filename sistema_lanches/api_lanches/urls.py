from django.urls import path
from .views import ClienteList, ClienteDetail, ProdutoList, ProdutoDetail

urlpatterns = [
    path('clientes/', ClienteList.as_view(), name='clientes-list'),
    path('clientes/<int:pk>/', ClienteDetail.as_view(), name='clientes-detail'),
    path('produtos/', ProdutoList.as_view(), name='produtos-list'),
    path('produtos/<int:pk>/', ProdutoDetail.as_view(), name='produtos-detail'),
]
