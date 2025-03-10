from rest_framework import serializers
from .models import CashFlow, Status, TypeCashFlow, Category, Subcategory


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TypeCashFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCashFlow
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class CashFlowSerializer(serializers.HyperlinkedModelSerializer):
    # делаем корректное отображение названий полей, а не их идентификаторов
    status = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Status.objects.all()
    )
    type_cash_flow = serializers.SlugRelatedField(
        slug_field='name',
        queryset=TypeCashFlow.objects.all()
    )
    category_cash_flow = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all()
    )
    subcategory_cash_flow = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Subcategory.objects.all()
    )

    class Meta:
        model = CashFlow
        fields = [
            'url',
            'created_at',
            'status',
            'type_cash_flow',
            'category_cash_flow',
            'subcategory_cash_flow',
            'amount',
            'comment',
        ]
        read_only_fields = ['created_at']

    # проверка на правильность подкатегории
    @staticmethod
    def validate(attrs):
        category_cash_flow = attrs.get('category_cash_flow')
        subcategory_cash_flow = attrs.get('subcategory_cash_flow')

        if subcategory_cash_flow and subcategory_cash_flow.category != category_cash_flow:
            raise serializers.ValidationError({
                'subcategory_cash_flow': 'Подкатегория должна принадлежать выбранной категории.'
            })
        return attrs

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['amount'] = f"{representation['amount']} ₽"
        return representation
