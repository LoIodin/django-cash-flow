from rest_framework import viewsets, permissions
from .serializers import (
    CashFlowSerializer,
    StatusSerializer,
    TypeCashFlowSerializer,
    CategorySerializer,
    SubcategorySerializer)
from .models import CashFlow, Status, TypeCashFlow, Category, Subcategory
from drf_spectacular.utils import extend_schema_view
from drf_spectacular.views import extend_schema, OpenApiParameter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CashFlowFilter
from decimal import Decimal


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TypeCashFlowViewSet(viewsets.ModelViewSet):
    queryset = TypeCashFlow.objects.all()
    serializer_class = TypeCashFlowSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


@extend_schema_view(
    list=extend_schema(
        summary='Получить список всех записей о движениях денежных средств'
    ),
    update=extend_schema(
        summary='Полное изменение существующей записи'
    ),
    create=extend_schema(
        summary='Создание новой записи о движении денежных средств'
    ),
    partial_update=extend_schema(
        summary='Частичное изменение существующей записи'
    ),
    retrieve=extend_schema(
        summary='Получить конкретную запись'
    ),
    destroy=extend_schema(
        summary='Удалить запись'
    )
)
class CashFlowViewSet(viewsets.ModelViewSet):
    queryset = CashFlow.objects.all().order_by('id')
    serializer_class = CashFlowSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head']
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CashFlowFilter
