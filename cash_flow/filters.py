import django_filters
from .models import CashFlow, Category, Subcategory, Status, TypeCashFlow


# фильтрация по дате, статусу, типу, категории и подкатегории
class CashFlowFilter(django_filters.FilterSet):
    # Фильтр по дате (диапазон)
    date_range = django_filters.DateFromToRangeFilter(
        field_name='created_at',
        label='Период дат (date_after и date_before)'
    )

    # Фильтр по статусу (выбор одного)
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        field_name='status',
        label='Статус'
    )

    # Фильтр по типу (выбор одного)
    type_cash_flow = django_filters.ModelChoiceFilter(
        queryset=TypeCashFlow.objects.all(),
        field_name='type_cash_flow',
        label='Тип'
    )

    # Фильтр по категории (выбор одного)
    category_cash_flow = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        field_name='category_cash_flow',
        label='Категория'
    )

    # Фильтр по подкатегории (автоматически зависит от категории)
    subcategory_cash_flow = django_filters.ModelChoiceFilter(
        queryset=Subcategory.objects.all(),
        field_name='subcategory_cash_flow',
        label='Подкатегория'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category_cash_flow' in self.data:
            category_id = self.data.get('category_cash_flow')
            if category_id:
                self.filters['subcategory_cash_flow'].queryset = Subcategory.objects.filter(
                    category_id=category_id
                )
            else:
                self.filters['subcategory_cash_flow'].queryset = Subcategory.objects.none()
        else:
            self.filters['subcategory_cash_flow'].queryset = Subcategory.objects.all()

    class Meta:
        model = CashFlow
        fields = ['date_range', 'status', 'type_cash_flow', 'category_cash_flow', 'subcategory_cash_flow']