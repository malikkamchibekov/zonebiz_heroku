from django.shortcuts import render, redirect

from .forms import ServiceForm
from .models import Service, Blog


def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,

    }
    return render(request, 'zonebiz/index.html', context)


def error(request):
    return render(request, 'zonebiz/404.html')


def about(request):
    return render(request, 'zonebiz/about.html')


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'zonebiz/blog.html', {'blogs': blogs})


def blog_post(request):
    return render(request, 'zonebiz/blog-post.html')


def contact(request):
    return render(request, 'zonebiz/contact.html')


def faq(request):
    return render(request, 'zonebiz/faq.html')


def portfolio_3(request):
    return render(request, 'zonebiz/portfolio-3-col.html')


def portfolio_4(request):
    return render(request, 'zonebiz/portfolio-4-col.html')


def portfolio_item(request):
    return render(request, 'zonebiz/portfolio-item.html')


def pricing(request):
    return render(request, 'zonebiz/pricing.html')


def services(request):
    services = Service.objects.all()
    return render(request, 'zonebiz/services.html', {'services': services})


def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ServiceForm()
    return render(request, 'zonebiz/create_service.html', {'form': form})
