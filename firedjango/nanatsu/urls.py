from django.urls import include,path, re_path
from . import views


urlpatterns = [
    path('signIn/',views.signIn,name="sign-in"),
    path('signIn/postsign/',views.postsignIn,name="post-sign-in")
    path('logOut/',views.logout,name="log-out")
]
