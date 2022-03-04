from django.urls import path
from blog import views

urlpatterns = [
    path("", views.start_page, name="start-page"),  # The initial page
    path("posts", views.posts, name="posts-page"),  # The page with the posts
    path("posts/<slug:slug>", views.individual_posts, name="individual-posts-page"),
    # A dynamic segment using <>.
]