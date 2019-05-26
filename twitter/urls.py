from django.conf.urls import url

from twitter import views


urlpatterns = [
    url(r'^$', views.TweetList.as_view() , name='tweet-list'),
    url(r'^create_tweet/$', views.CreateTweet.as_view() , name='create-tweet'),
    url(r'^login_user/$', views.LoginUser.as_view() , name='login-user'),
    url(r'^create_user/$', views.CreateUser.as_view() , name='create-user'),
    url(r'^user_view/(?P<user_pk>(\d)+)$', views.UserView.as_view() , name='user-view'),
    url(r'^tweet_view/(?P<tweet_pk>(\d)+)$', views.TweetView.as_view() , name='tweet-view'),


]