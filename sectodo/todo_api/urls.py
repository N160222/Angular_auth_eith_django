from django.urls import include, path


urlpatterns = [
    # path('home/',home),
    path('api-auth/', include('rest_framework.urls'))
]