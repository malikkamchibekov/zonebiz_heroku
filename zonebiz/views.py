from django.shortcuts import render


def index(request):
    return render(request, 'zonebiz/index.html')


def error(request):
    return render(request, 'zonebiz/404.html')


def about(request):
    return render(request, 'zonebiz/about.html')


def blog(request):
    return render(request, 'zonebiz/blog.html')


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
    return render(request, 'zonebiz/services.html')