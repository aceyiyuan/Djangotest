import django_filters
from django_filters import DateFilter,CharFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
	start_date=DateFilter(field_name="date_created",lookup_expr="gte")
	end_date=DateFilter(field_name="date_created",lookup_expr="lte")
	note=CharFilter(field_name='note', lookup_expr="icontains")
	class Meta:
		model=Order
		fields="__all__"
		exclude=['customer','date_created',]
		

#product_name filter search by the name of the product by typing without note
#product__name=CharFilter(field_name='product_name', lookup_expr='icontains')