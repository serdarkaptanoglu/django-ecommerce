from django.shortcuts import render, redirect, get_object_or_404
from . models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignUpForm


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Başarıyla Giriş Yaptınız...")
            return redirect('home')
        else:
            messages.info(request, "Kullanıcı Adı veya Parola Hatalı...")
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "Çıkış yaptınız...")
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Başarıyla Kayıt Oldunuz...")
            return redirect('home')
        else:
            messages.info(request, "Hatalı bir işlem yaptınız...")
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})


def category(request, name):
    name = name.replace('-', ' ')
    try:
        category = Category.objects.get(name=name)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'category': category, 'products': products})
    except Category.DoesNotExist:
        messages.info(request, 'Böyle bir kategori yoktur..')
        return redirect('home')


def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {'categories': categories})
