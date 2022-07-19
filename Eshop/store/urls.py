from django.urls import path
from .import views
from .views import Login,Signup,Index
urlpatterns = [

    # path('',views.index,name='homepage'),

    path('',Index.as_view(),name='homepage'),

    # path('signup',views.signup),

    path('signup',Signup.as_view()),

    # path('login',views.login),

    path('login',Login.as_view())


]