from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from cash_flow import views


router = routers.DefaultRouter()
router.register(r'statuses', views.StatusViewSet)
router.register(r'types', views.TypeCashFlowViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'subcategories', views.SubcategoryViewSet)
router.register(r'cash-flows', views.CashFlowViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
