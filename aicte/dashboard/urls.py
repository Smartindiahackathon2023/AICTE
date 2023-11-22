from django.urls import path
from .views import index,developerpanel,integrate_with_google_calendar,dashboard,tohtml
# from .views import signup,verify,login,logout_view



urlpatterns = [
    path('',index,name='homepage'),
    path('dashboard/',dashboard,name='dashboard'),
    path('dashboard/develop/',developerpanel,name="developerpanel"),
    path('googlemeet/',integrate_with_google_calendar,name="googlemeet"),
    path('tohtml/',tohtml,name="tohtml")
 ]