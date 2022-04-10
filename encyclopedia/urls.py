from django.urls import path,re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/display", views.random_entry, name="displayrandom"),
    path("display/", views.search, name="search"),
    re_path(r'^wiki/(.+)/$', views.show_entry, name="entry"),
    path("/creating", views.create_entry, name="new"),
    path("save/", views.saving_entry, name="save"),
    re_path(r'^save/wiki/(.+)$',views.show_entry,name="entry"),
    re_path(r'edit/(.+)$',views.editing_entry, name="editing"),
    re_path(r'edit/(.+)/(.+)$',views.editing_entry, name="editing"),
    path("edit/",views.saved_entry,name="saved"),
]
