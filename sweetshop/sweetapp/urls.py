from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView

urlpatterns = [
    path('', views.index, name='home'),  # Homepage
    path('products/', views.product_list, name='products'),  # Product list
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Add to cart
    path('cart/', views.cart, name='cart'),  # View cart
    path('checkout/', views.checkout, name='checkout'),  # Checkout
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout
    path('register/', views.register, name='register'),  # Register
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Custom login page
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('order-success/', views.order_success, name='order_success'),


]
