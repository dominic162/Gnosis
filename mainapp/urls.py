from django.urls import path
from mainapp import views 
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.auth_login,name="login"),
    path('signup',views.auth_signup,name="signup"),
    path('logout',views.auth_logout,name="logout")
]   

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)