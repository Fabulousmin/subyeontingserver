from django.urls import include, path

urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('userinfo/', include('userinfo.urls')),
    path('profile/', include('profiles.urls')),
    path('chat/', include('chatapp.urls')),
    path('matching/',include('matching.urls')),
    ]
