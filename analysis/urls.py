from django.urls import path
from analysis import views


from django.conf.urls import url

urlpatterns=[
    path('analysis/', views.analysis),
    #url(r'^index/',views.index)#配置当访问index/时去调用views下的index方法
]