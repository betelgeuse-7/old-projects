from django.urls import path
from .views import index, register, sign_in, sign_out, logged_in, send_a_post,delete_a_post

app_name = 'usermodel'

#do not forget adding app_name

urlpatterns = [
    path('', index, name = 'index_page'),
    path('registration/', register, name = 'registration_page'),
    path('login/', sign_in, name = 'login_page'),
    path('logout/', sign_out, name = 'logout_page'),
    path('success/', logged_in, name = 'successful_login_page'),
    path('posts/', send_a_post, name = 'post_page'),
    path('posts/delete/<int:post_id>', delete_a_post, name = 'delete_post_page'),
]