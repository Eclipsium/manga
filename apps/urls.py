from django.conf.urls import url
from django.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from apps.manga_api.views import MangaViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="MangaReader API",
      default_version='v1',
      description="MangaReader API endpoint",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="abiogenesis70ru@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('manga', MangaViewSet)
# router.register('person', MangaPersonViewSet)

urlpatterns = [
    # ...
    # Use the `get_schema_view()` helper to add a `SchemaView` to project URLs.
    #   * `title` and `description` parameters are passed to `SchemaGenerator`.
    #   * Provide view name for use with `reverse()`.

    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^', include(router.urls)),
    # path('manga/<slug>/', MangaDetailView.as_view()),
]
