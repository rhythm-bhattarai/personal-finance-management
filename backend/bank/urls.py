from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'accounts', views.AccountDetailsViewSet, basename='accountdetails')
router.register(r'amounts', views.AmountDetailsViewSet, basename='amountdetails')

urlpatterns = router.urls