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
    path("posts/new/", views.PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    path("posts/<int:post_id>/comments/new/", views.add_comment, name="add_comment"),
    path("comments/<int:comment_id>/edit/", views.edit_comment, name="edit_comment"),
    path(
        "comments/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"
    ),
    path("search/", views.search_posts, name="search_posts"),
    path("tags/<str:tag_name>/", views.posts_by_tag, name="posts_by_tag"),
]
