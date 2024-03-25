from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="Home"),
    path("post/",views.post,name="post"),
    path("loginp/",views.loginp,name="login"),
    path("create_account/",views.create_account,name="create_account")
]