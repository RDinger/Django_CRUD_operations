from django.conf.urls import url
from basic_app import views

# for the injection notation 
app_name= 'basic_app'

urlpatterns =[
	url(r'^$', views.SchoolListView.as_view(), name= 'list'),
	url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(),name='detail'),
	url(r'^create/', views.SchoolCreateView.as_view(),name='create'),
	url(r'^add_student/', views.StudentCreateView.as_view(),name='add'),
	url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(),name='update'),
	url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(),name='delete')
]