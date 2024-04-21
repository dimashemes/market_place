from django.contrib import admin
from django.urls import path
from market import views
from django.conf.urls.static import static
from shop import settings
from market import views_auth

app_name = 'market'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('main_page/', views.main_page, name='main_page'),
    path('register/', views_auth.registration, name='register'),
    path('login/', views_auth.login_view, name='login'),
    path('logout/', views_auth.logout_view, name='logout'),
    path('account/', views.account, name='account'),
    path('add/', views.ProductCreateView.as_view(), name='product_add'),
    path('upload/', views.upload_product, name='upload_product'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/', views.search_product, name='search_product'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add_to_favorite/<int:product_id>/', views.add_to_favorite, name='add_to_favorite'),
    path('remove_from_favorite/<int:favorite_item_id>/', views.remove_from_favorite, name='remove_from_favorite'),
    path('cart/', views.cart_view, name='cart_view'),
    path('favorites/', views.favorite_view, name='favorite_view'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_favorite/<int:product_id>/', views.add_to_favorite, name='add_to_favorite'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)