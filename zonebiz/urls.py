from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('faq/', faq, name='faq'),
    path('404/', error, name='404'),
    path('pricing/', pricing, name='pricing'),
    path('portfolio-3-col/', portfolio_3, name='portfolio-3-col'),
    path('portfolio-4-col/', portfolio_4, name='portfolio-4-col'),
    path('portfolio-item/', portfolio_item, name='portfolio-item'),
    path('blog/', blog, name='blog'),
    path('blog-post/', blog_post, name='blog-post'),
    path('contact/', contact, name='contact')
]

