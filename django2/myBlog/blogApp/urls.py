from django.urls import path
from .views import (IndexPage, posts_view, SignUpView, PostCommentsView,
                    sign_in, sign_out, like, CategoryView, PostUpdate, category_detail_view,
                    profile_detail_view, search_topic, new_topic, delete_a_post,
                    follow_user, unfollow_user, search_a_user)

app_name = 'blogApp'

urlpatterns = [
    path('', IndexPage.as_view(), name='index_page'),
    path('register/', SignUpView.as_view(), name='register_page'),
    path('login/', sign_in, name='login_page'),
    path('logout/', sign_out, name='logout_page'),
    path('like/<int:pk>', like, name='like_post'),
    path('profile/<int:id>', profile_detail_view,
         name='profile_detail_page'),
    path('topics/', CategoryView.as_view(), name='category_page'),
    path('topic/<int:id>/',
         category_detail_view, name='category_detail_page'),
    path('searcht/', search_topic, name='search_topic_page'),
    path('createt/', new_topic, name='new_topic_page'),
    path('post-detail/<int:pk>', PostCommentsView.as_view(),
         name='post_detail_page'),
    path('post-update/<int:pk>', PostUpdate.as_view(), name='post_update_page'),
    path('delete-post/<int:id>/', delete_a_post, name='delete_post_page'),
    path('follow/<int:id>/', follow_user, name='follow_user_page'),
    path('unfollow/<int:id>/', unfollow_user, name='unfollow_user_page'),
    path('search-for-users/', search_a_user, name='search_users_page'),
]
