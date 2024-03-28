from rest_framework import serializers
from cba.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'Cid', 'P_Date', 'Category', 'Price', 'Quantity', 'TPAmt', 'Payment', 'Returns', 'Name', 'Age', 'Gender', 'Churn']