from django.conf.urls import url

from twitter import views


urlpatterns = [
    url(r'^$', views.TweetList.as_view(), name='tweet-list'),
    url(r'^login_user/$', views.LoginUser.as_view(), name='login-user'),
    url(r'^create_user/$', views.CreateUser.as_view(), name='create-user'),
    url(r'^user_view/(?P<pk>(\d)+)$', views.UserView.as_view(), name='user-view'),
    url(r'^tweet_view/(?P<tweet_pk>(\d)+)$', views.TweetView.as_view(), name='tweet-view'),
    url(r'^user_messages$', views.UserMessages.as_view(), name='user-messages'),
    url(r'^read_message/(?P<pk>(\d)+)$', views.ReadMessage.as_view(), name='read-message'),
    url(r'^change_user_password$', views.ChangeUserPassword.as_view(), name='change-password'),


]