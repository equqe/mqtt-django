from django.urls import path, include
from apps.users import views

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('account/register/', views.RegisterView.as_view(), name='register'),
    path('', views.index_view, name='index')
]
