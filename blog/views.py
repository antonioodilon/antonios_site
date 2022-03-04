from datetime import date
from django.shortcuts import render

# Each post will be a dictionary:
posts_list = [
    {
        "slug": "barbecue",
        "image": "barbecue.jpg",
        "author": "Antonio",
        "date": date(2022, 2, 1),
        "title": "I love meat!",
        "excerpt": """Did you know that meat is one of the most nutrient-dense foods in
         the world? :D""",
        "content": "Beatae at debitis quam. Voluptate fugiat deserunt sit blanditiis eius?",
    },
    {
        "slug": "weightlifting",
        "image": "bent_press.jpg",
        "author": "Antonio",
        "date": date(2022, 2, 11),
        "title": "Natural Bodybuilding!",
        "excerpt": """I consider myself a Natural Bodybuilder! Aesthetics is a fundamental
        part of my life, but I also want to be healthy. This is why I don't take steroids!""",
        "content": "Beatae at debitis quam. Voluptate fugiat deserunt sit blanditiis eius?",
    },
    {
        "slug": "coding",
        "image": "coding.png",
        "author": "Antonio",
        "date": date(2022, 1, 25),
        "title": "Programming",
        "excerpt": """I simply love programming! Currently I program in Python, but I also
        intend to study other languages, such as C.""",
        "content": "Beatae at debitis quam. Voluptate fugiat deserunt sit blanditiis eius?",
    },
]


def get_date(post: dict):
    return post['date']


# A function for the starting page:
def start_page(request):
    sorted_posts = sorted(posts_list, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {"posts": latest_posts})


# A function for all the posts:
def posts(request):
    return render(request, 'blog/all_posts.html', {"posts_list": posts_list})


# A function for the individual posts:
def individual_posts(request, slug):
    for post in posts_list:
        if post['slug'] == slug:
            post_to_access = post
    # post_to_access = next(post for post in posts_list if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {"individual_post": post_to_access})