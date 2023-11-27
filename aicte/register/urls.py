from django.urls import path
from .views import signup,login_view
# from .views import signup,verify,login,logout_view



urlpatterns = [
    path('',signup,name='signup'),
    path('login/',login_view,name="loginpage")
#     path('login/',login,name='login'),
#     path('logout/',logout_view,name='logout'),
#     path('verify/<str:token>/',verify,name='verification')
 ]