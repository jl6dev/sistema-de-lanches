from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cliente, Produto
from .serializers import ClienteSerializer, ProdutoSerializer


def get(request):
    clientes = Cliente.objects.all()
    serializer = ClienteSerializer(clientes, many=True)
    return Response(serializer.data)


def post(request):
    serializer = ClienteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteList(APIView):
    pass


def get(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def delete(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


class ClienteDetail(APIView):
    pass


def get(request):
    produtos = Produto.objects.all()
    serializer = ProdutoSerializer(produtos, many=True)
    return Response(serializer.data)


def post(request):
    serializer = ProdutoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProdutoList(APIView):
    pass


def get(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)
    except Produto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def delete(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Produto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


class ProdutoDetail(APIView):
    pass

