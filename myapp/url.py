from django.conf.urls import include, url
from myapp import views
from myapp.views import StaticView
from django.views.generic import TemplateView
from django.urls import path,include, re_path
urlpatterns = [path('hello/', views.hello, name = 'hello'),
               path('morning/', views.morning, name = 'morning'),
               path('days/', views.days, name = 'days'),
               path('main/', views.main_h, name = 'main'),
               path('hello_3/', views.hello_3, name = 'hello_3'),
               
               path('CRUD/', views.crudops, name = 'CRUD'),
               path('article/<int:articleId>/', views.viewArticle_2, name = 'articles'),
               path('article/<int:year>/<int:month>/', views.viewArticles_2, name = 'articles_2'),
              # re_path(r'^simpleemail/(?P<emailto>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+)/$',views.sendSimpleEmail , name = 'sendSimpleEmail'),
             #  re_path(r'^massemail/(?P<emailto>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+)/(?P<emailto>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+)/$',views.sendMassEmail , name = 'send_Mass_Email'),

               path('static/',StaticView.as_view(),),
               path('login/',views.login,name='conn'),
               path('admin/',views.admin,name='admin')

            ]