from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.registration.views import SocialAccountListView




urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('accounts/', include('accounts.urls')),

    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/social/', include('allauth.socialaccount.providers.google.urls')),
    path('jwt/', include('JWT.urls')),
    path('test/', include('house.urls')),
    path('', include('authentication.urls')),

]

# urlpatterns = [path('api/', include(urlpatterns))]



# https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=http://localhost:8000/accounts/dj-rest-auth/google/&prompt=consent&response_type=code&client_id=640391091582-5id7vu51go25k5k15esej06b9qcshvpg.apps.googleusercontent.com&scope=openid%20email%20profile&access_type=offline
# https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=http://localhost:8000/accounts/dj-rest-auth/google/&prompt=consent&response_type=code&client_id=640391091582-5id7vu51go25k5k15esej06b9qcshvpg.apps.googleusercontent.com&scope=openid%20email%20profile%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuser.birthday.read&access_type=offline&service=lso&o2v=2&flowName=GeneralOAuthFlow
