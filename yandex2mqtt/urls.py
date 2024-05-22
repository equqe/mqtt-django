from django.contrib import admin
from django.urls import path, include
from apps.users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('yandex/v1.0', include("apps.yandex.urls")),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('account/register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.index_view, name='index'),
    path('alice/', views.alice_view, name='alice'),
    path('doc/', views.doc_view, name='doc'),
    path('support/', views.support_view, name='support'),
    path('wait/', views.wait_view, name='wait'),
    path('ajax/ajax_pairing_key_renew/', views.ajax, name='ajax'),
]
