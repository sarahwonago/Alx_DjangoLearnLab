from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Authentication (if not already present)
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="blog/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="blog/logout.html"),
        name="logout",
    ),
    path("register/", views.register, name="register"),  # if you have register view
    # Blog post CRUD
    path("posts/", views.PostListView.as_view(), name="post-list"),
    path("post/new/", views.PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    path(
        "post/<int:pk>/comments/new/",
        views.CommentCreateView.as_view(),
        name="add_comment",
    ),
    path(
        "comment/<int:pk>/update/",
        views.CommentUpdateView.as_view(),
        name="edit_comment",
    ),
    path(
        "comment/<int:pk>/delete/",
        views.CommentDeleteView.as_view(),
        name="delete_comment",
    ),
    path("search/", views.search_posts, name="search_posts"),
    path("tags/<str:tag_name>/", views.posts_by_tag, name="posts_by_tag"),
]
