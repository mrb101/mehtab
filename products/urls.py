from django.conf.urls import url

from views import (
    ProductList,
    CategoryCreate,
    CategoryDetail,
    CategoryUpdate,
    ProductDetail,
)

urlpatterns = [
    #url(r'^$', ProductList.as_view(), name='product_list'),
    #url(r'^category/new', CategoryCreate.as_view(), name='category_create'),
    #url(r'^(?P<slug>[-\w]+)/', ProductDetail.as_view(), name='product_detail'),
]
