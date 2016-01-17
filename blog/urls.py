from django.conf.urls import include, url
from . import views

urlpatterns = [
    #creating URL to published post list
    url(r'^$', views.post_list, name='post_list'),
    #creating URL to a post's detail
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    #creating URL to a form
    url(r'^post/new/$', views.post_new, name='post_new'),
    #creating URL to edit version of form
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    #creating URL to the page having list of draft posts
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    #creating URL to the post publishing page
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    #creating URL for delete page
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    #creating URL for letting readers write comments
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    #creating URL for approving the reader's comment
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    #creating URL for removing the reader's comment
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),

]