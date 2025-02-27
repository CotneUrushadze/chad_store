from django.urls import path, include
from products.views import ReviewViewSet, ProductViewSet, FavoriteProductViewSet, CartViewSet, ProductTagViewSet, ProductImageViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('cart', CartViewSet)
router.register('favorite_products', FavoriteProductViewSet)
router.register('tags', ProductTagViewSet)


products_router = routers.NestedDefaultRouter(
    router,
    'products',
    lookup = 'product'
)
products_router.register('images', ProductImageViewSet, basename='product-images')
products_router.register('reviews', ReviewViewSet, basename='product-reviews')






urlpatterns = [
    path("", include(router.urls)),
    path("", include(products_router.urls)),
    
    
    # path('products/', ProductViewSet.as_view({'get':'list', 'post':'create'}), name="products"),
    # path('products/<int:pk>/', ProductViewSet.as_view({'get':'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete':'destroy'}), name='product'),
    # path('products/<int:product_id>/reviews/', ReviewViewSet.as_view(), name="reviews"),
    # path('favorite_products/', FavoriteProductViewSet.as_view({'get':'list', 'post':'create'}), name="favorite_products"),
    # path('favorite_products/<int:pk>/', FavoriteProductViewSet.as_view({'get':'retrieve' , 'delete':'destroy'}), name="favorite_product"),
    # path('cart/', CartViewSet.as_view(), name="cart"),
    # path('producttag/', ProductTagViewSet.as_view(), name="producttags"),
    # path('products/<int:product_id>/images/', ProductImageViewSet.as_view({'get':'list', 'post':'create'}), name="product-images"),
    # path('products/<int:product_id>/images/<int:pk>/', ProductImageViewSet.as_view({'get':'retrieve', 'delete':'destroy'}), name="product-image"),
    
]