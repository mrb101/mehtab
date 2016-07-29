"""mehtab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from products import views as productsviews

urlpatterns = [
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', productsviews.IndexTemplate.as_view(), name='index'),
    url(r'^contact/$', productsviews.ContactTemplate.as_view(), name='contact'),
    url(r'^categories/$', productsviews.CategoryList.as_view(), name='category_list'),
    url(r'^categories/new', productsviews.CategoryCreate.as_view(), name='category_create'),
    url(r'^categories/(?P<slug>[-\w]+)/show$', productsviews.CategoryDetail.as_view(), name='category_detail'),
    url(r'^categories/(?P<slug>[-\w]+)/$', productsviews.CategoryProductsList.as_view(), name='category_product_list'),
    url(r'^categories/(?P<slug>[-\w]+)/update', productsviews.CategoryUpdate.as_view(), name='category_update'),
    url(r'^products/$', productsviews.ProductList.as_view(), name='product_list'),
    url(r'^products/new', productsviews.ProductCreate.as_view(), name='product_create'),
    url(r'^products/(?P<slug>[-\w]+)/$', productsviews.ProductDetail.as_view(), name='product_detail'),
    url(r'^products/(?P<slug>[-\w]+)/update', productsviews.ProductUpdate.as_view(), name='product_update'),

]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
