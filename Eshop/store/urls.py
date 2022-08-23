import imp
from django.urls import path
from .import views
from .import views
from .views import Login,Signup,Index,Cart,Checkout,OrderView
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('',views.front,name='front'),
    path('store',Index.as_view(),name='homepage'),
    path('signup',Signup.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
    path('logout',views.logout,name='logout'),
    path('cart',Cart.as_view(),name='cart'),
    path('check-out',Checkout.as_view(),name='check-out'),
    path('orders',auth_middleware(OrderView.as_view()),name='orders')

]