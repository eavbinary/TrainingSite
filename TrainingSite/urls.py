from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from graphene_django.views import GraphQLView

urlpatterns = [

    path('', include('core.urls', namespace='core')),
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    path("graphql", GraphQLView.as_view(graphiql=True)),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='core:home')),
    path('accounts/profile/', RedirectView.as_view(pattern_name='core:home', permanent=True)),
]
