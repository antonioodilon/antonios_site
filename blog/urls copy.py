from django.urls import path
from blog import views

urlpatterns = [
    path("", views.start_page, name="start-page"),  # The initial page
    path("posts", views.posts, name="posts-page"),  # The page with the posts
    path("posts/<slug:slug>", views.individual_posts, name="individual-posts-page"),
    # A dynamic segment using <>.
    # The name can be whatever we want, but this concept is called slug. It will be 
    # something like posts/name-of-post-1, posts/name-of-post-2, posts-name-of-post-3,
    # and so on.
    # slug:slug checks if the post has the vanilla format with no special characters, just
    # numbers, dashes and text. See django documentation if in doubt
]