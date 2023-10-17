from django.urls import path,include
from users import views 


app_name='users'


urlpatterns = [
    path('login/',views.login, name="login" ),
    path('sign/',views.sign, name="sign" ),
]