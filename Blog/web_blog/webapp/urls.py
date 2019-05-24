from django.urls import path,include
from django.conf.urls import url
from webapp import views



urlpatterns = [
    url(r'^blog/', views.DashBoard.as_view(),),
    url(r'^all-blogs/$',views.AllBlogView.as_view(),name="all_blogs"),
    url(r'^single_blog/(?P<pk>\d+)/$',views.SingleBlogView.as_view(),name="single_blog")


]
