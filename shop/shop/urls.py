from django.urls import path

from accounts import views as account_views
from catalog import views as catalog_views
from orders import views as order_views

urlpatterns = [
    path("api/products/", catalog_views.product_list),
    path("api/products/<str:sku>/", catalog_views.product_detail),
    path("api/checkout/", order_views.checkout),
    path("api/orders/<int:order_id>/", order_views.order_detail),
    path("api/password-reset/", account_views.request_password_reset),
]
