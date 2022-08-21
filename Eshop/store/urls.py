from django.urls import path
from .import views
from .import views
from .views import Login,Signup,Index,Cart
urlpatterns = [
    path('',Index.as_view(),name='homepage'),
    path('signup',Signup.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
    path('logout',views.logout,name='logout'),
    path('cart',Cart.as_view(),name='cart')




]