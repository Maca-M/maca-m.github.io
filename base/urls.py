from django.urls import path
from .views import ListProducts, DetailProduct, NewProduct, EditProduct, DeleteProduct, Login
from django.contrib.auth.views import LogoutView

urlpatterns = [path('', ListProducts.as_view(), name='products'),
               path('login/', Login.as_view(), name='login'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
               path('product/<int:pk>', DetailProduct.as_view(), name='product'),
               path('new-product/', NewProduct.as_view(), name='new-product'),
               path('edit-product/<int:pk>', EditProduct.as_view(), name='edit-product'),
               path('delete-product/<int:pk>', DeleteProduct.as_view(), name='delete-product')]