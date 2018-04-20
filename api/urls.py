from django.urls import path
from . import views

urlpatterns = [
	path('', views.blog_list, name="blog_list"),
	# path('add', views.blog_add, name="blog_add"),
	# path('<int:blog_id>/delete', views.blog_delete, name="blog_delete"),
	path('<int:blog_id>', views.blog_detail, name="blog_detail"),
	# path('<int:blog_id>/details/edit', views.blog_edit, name="blog_edit"),

]
