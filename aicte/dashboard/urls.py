from django.urls import path
from .views import index,developerpanel,integrate_with_google_calendar,dashboard,getmsgs
# from .views import signup,verify,login,logout_view



urlpatterns = [
    path('',index,name='homepage'),
    path('dashboard/',dashboard,name='dashboard'),
    path('dashboard/develop/',developerpanel,name="developerpanel"),
    path('googlemeet/',integrate_with_google_calendar,name="googlemeet"),
    path('getmsg/<int:senderid>/<int:recieverid>',getmsgs,name='getmsgs'),
 ]