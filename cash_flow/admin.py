from django.contrib import admin
from .models import CashFlow, Category, Subcategory, TypeCashFlow, Status


@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'status',
        'type_cash_flow',
        'category_cash_flow',
        'subcategory_cash_flow',
        'amount',
    ]

    list_select_related = [
        'status',
        'type_cash_flow',
        'category_cash_flow',
        'subcategory_cash_flow',
    ]

    list_filter = [
        'created_at',
        'status',
        'type_cash_flow',
        'category_cash_flow',
        'subcategory_cash_flow',
    ]

    search_fields = [
        'amount',
        'comment',
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeCashFlow)
class TypeCashFlowAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass
