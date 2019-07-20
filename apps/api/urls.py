from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

API_TITLE = "API"
API_DESCRIPTION = "Web API"
app_name = 'api'

schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('webapi.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('schema/', schema_view),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('swagger-docs/', get_swagger_view()),
]
