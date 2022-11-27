from rest_framework.routers import DefaultRouter



from products.viewsets import ProductViewSet, viewsets

router = DefaultRouter()
router.register('product-abc', ProductViewSet, basename='product')
print(router.urls)
urlpatterns = router.urls
