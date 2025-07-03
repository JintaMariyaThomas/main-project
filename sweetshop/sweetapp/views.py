from django.shortcuts import render, redirect
from .models import Product
from .forms import OrderForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomLoginForm

# Homepage view (no authentication required)
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

# Product list view (accessible to all users)
def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'products.html', {'products': products, 'query': query})

# Add product to cart (for all users, stored in session)
def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    cart.append(product_id)
    request.session['cart'] = cart
    return redirect('cart')

# View cart (accessible to all users)
def cart(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    total = sum(p.price for p in products)
    return render(request, 'cart.html', {'products': products, 'total': total})

# Checkout (authentication required to proceed)
def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['cart'] = []  # Clear cart
            messages.success(request, "✅ Payment successful! Your order has been placed.")
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'checkout.html', {'form': form})

def order_success(request):
    return render(request, 'order_success.html')
# About page view
def about(request):
    return render(request, 'about.html')

# Contact page view
def contact(request):
    return render(request, 'contact.html')

# Register new user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Custom login view with messages
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm

    def form_valid(self, form):
        messages.success(self.request, f"Welcome, {form.get_user().username}!")
        return super().form_valid(form)
    
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
        request.session['cart'] = cart
        messages.info(request, "Item removed from cart.")
    return redirect('cart')


def add_to_wishlist(request, product_id):
    wishlist = request.session.get('wishlist', [])
    if product_id not in wishlist:
        wishlist.append(product_id)
        request.session['wishlist'] = wishlist
        messages.success(request, "Item added to wishlist.")
    return redirect('products')


def remove_from_wishlist(request, product_id):
    wishlist = request.session.get('wishlist', [])
    if product_id in wishlist:
        wishlist.remove(product_id)
        request.session['wishlist'] = wishlist
        messages.info(request, "Item removed from wishlist.")
    return redirect('wishlist')


def wishlist(request):
    wishlist = request.session.get('wishlist', [])
    products = Product.objects.filter(id__in=wishlist)
    return render(request, 'wishlist.html', {'products': products})


