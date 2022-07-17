from django.urls import path
from .import views
from .views import Login
urlpatterns = [
    path('',views.index,name='homepage'),
    path('signup',views.signup),
    # path('login',views.login),
    path('login',Login.as_view())


]