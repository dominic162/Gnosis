from django.urls import path
from mainapp import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('',    views.home, name="home"),
    path('login',   views.auth_login,   name="login"),
    path('signup',  views.auth_signup,  name="signup"),
    path('logout',  views.auth_logout,  name="logout"),
    path('all-doubts',  views.allques,  name="all_doubts"),
    path('new-doubt',   views.ask,  name="ask_doubt"),
    path('doubt/<int:pk>',  views.show_doubt, name="show_doubt"),
    path('add-book',    views.add_book, name="add_book"),
    path('all-books',   views.all_books,    name="all_books"),
    path('book/<int:pk>',   views.book_view,    name="book_view"),
    path('users/<slug>',views.user_info, name ="user_info")

]   

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)