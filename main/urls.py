from django . urls import path
from.views import *
urlpatterns =[
    path('',index_view, name='index_url'),
    path('search/', search_view, name='search_url'),
    path('about/', about_view, name='about_url'),
    path('contact/', contact_view, name='contact_url'),
    path('category/<int:pk>/', category_view, name='category_url'),
    path('blog-detayl/<int:pk>/', single_view, name='single_url'),
    path('create-blog/', create_blog_view, name='create_blog_url'),
    path('blog-update/<int:pk>/', update_blog_view, name='update_url'),
    path('blog-delete/<int:pk>/', delete_view, name='delete_url'),
]
