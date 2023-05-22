
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
]

urlpatterns += i18n_patterns(
    path('app/', include('app.urls'))
)
