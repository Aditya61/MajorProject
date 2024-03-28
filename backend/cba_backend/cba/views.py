from django.shortcuts import render
from rest_framework import generics
from cba.models import Customer
from cba.serializers import CustomerSerializer

# Views

class CustomerViewById(generics.ListAPIView):
    def get_queryset(self):
        return Customer.objects.filter(Cid=self.kwargs['Cid'])
    
    serializer_class = CustomerSerializer

class CustomerViewByProductCategory(generics.ListAPIView):
    def get_queryset(self):
        return Customer.objects.filter(Category=self.kwargs['Category'])
    
    serializer_class = CustomerSerializer

class CustomerViewByPaymentMethod(generics.ListAPIView):
    def get_queryset(self):
        return Customer.objects.filter(Payment=self.kwargs['Payment'])
    
    serializer_class = CustomerSerializer

class CustomerViewByGender(generics.ListAPIView):
    def get_queryset(self):
        return Customer.objects.filter(Gender=self.kwargs['Gender'])
    
    serializer_class = CustomerSerializer

class CustomerViewByAge(generics.ListAPIView):
    def get_queryset(self):
        return Customer.objects.filter(Age__gte=self.kwargs['stAge'],Age__lt=self.kwargs['endAge'])
    
    serializer_class = CustomerSerializer

class CustomerViewByPurchaseMonth(generics.ListAPIView):
    def get_queryset(self):
        return Customer.objects.filter(P_Date__contains="-"+self.kwargs['Month']+"-")

    serializer_class = CustomerSerializer

class CustomerViewByPurchaseYear(generics.ListAPIView):
    def get_queryset(self):
        return Customer.objects.filter(P_Date__contains=self.kwargs['Year']+"-")

    serializer_class = CustomerSerializer

class CustomerViewByPurchaseDate(generics.ListAPIView):
    def get_queryset(self):
        return Customer.objects.filter(P_Date__contains=self.kwargs['Date']+"T")

    serializer_class = CustomerSerializer

class CustomerViewByTotalPurchaseAmount(generics.ListAPIView):
    def get_queryset(self):
        return Customer.objects.filter(TPAmt__gte=self.kwargs['stTPAmt'],TPAmt__lt=self.kwargs['endTPAmt'])
    
    serializer_class = CustomerSerializer

class CustomerViewByReturnStatus(generics.ListAPIView):
    def get_queryset(self):
        return Customer.objects.filter(Returns=self.kwargs['Returns'])
    
    serializer_class = CustomerSerializer

class CustomerViewByChurnStatus(generics.ListAPIView):
    def get_queryset(self):
        return Customer.objects.filter(Churn=self.kwargs['Churn'])
    
    serializer_class = CustomerSerializer