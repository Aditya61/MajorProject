from django.urls import path
from cba.views import *

urlpatterns = [
    path('customers/<int:Cid>/', CustomerViewById.as_view()),
    path('customers/ProductCategory/<Category>/', CustomerViewByProductCategory.as_view()),
    path('customers/PaymentMethod/<Payment>/', CustomerViewByPaymentMethod.as_view()),
    path('customers/Gender/<Gender>/', CustomerViewByGender.as_view()),
    path('customers/Age/<int:stAge>-<int:endAge>/', CustomerViewByAge.as_view()),
    path('customers/P_Date/Month/<Month>/', CustomerViewByPurchaseMonth.as_view()),
    path('customers/P_Date/Year/<Year>/', CustomerViewByPurchaseYear.as_view()),
    path('customers/P_Date/Date/<Date>/', CustomerViewByPurchaseDate.as_view()),
    path('customers/TPAmt/<int:stTPAmt>-<int:endTPAmt>/', CustomerViewByTotalPurchaseAmount.as_view()),
    path('customers/Returns/<int:Returns>/', CustomerViewByReturnStatus.as_view()),
    path('customers/Churn/<int:Churn>/',CustomerViewByChurnStatus.as_view())
]