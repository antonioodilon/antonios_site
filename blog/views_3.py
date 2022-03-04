from datetime import date
from django.shortcuts import render

# Each post will be a dictionary:
posts_list = [
    {
        "slug": "barbecue",
        "image": "barbecue.jpg",
        "author": "Antonio",
        "date": date(2022, 2, 1),
        "title": "Meat Eating",
        "excerpt": """Did you know that meat is one of the most nutrient-dense foods in
         the world? :D""",
        "content": "Beatae at debitis quam. Voluptate fugiat deserunt sit blanditiis eius?",
    },
    {
        "slug": "weightlifting",
        "image": "bent_press.jpg",
        "author": "Antonio",
        "date": date(2022, 2, 11),
        "title": "Natural Bodybuilding",
        "excerpt": """I am a Natural Bodybuilder! Aesthetics is a fundamental part of my life,
        but I also want to be healthy. This is why I don't take steroids!""",
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
# Take a look at post.html, and notice that there we don't use [] square brackets to access
# keys' values in a dictionary. Rather, we use dot notation -> post.title, post.excerpt etc

# In post.html the line with <img src="{% static 'blog/images/'|add:post.image %}" alt="Post_Image" />
# has a filter: |add:post.image

def get_date(post: dict):
    return post['date']  # Since post is a dictionary, we want to return this dictionary's values
    # Another option:
    # return post.get('date')


# A function for the starting page:
def start_page(request):
    sorted_posts = sorted(posts_list, key=get_date)  # We don't need to write get_date() with the
    # parentheses because we don't want Python to execute the function. Instead we just point
    # at get_date
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {"posts": latest_posts})  # Dictionaries can be
    # returned in functions!


# A function for all the posts:
def posts(request):
    return render(request, 'blog/all_posts.html')


# A function for the individual posts:
def individual_posts(request, slug):  # We need to make sure that this function accepts
    # the slug argument, because in the global urls.py we have "posts/<slug:slug>"
    return render(request, 'blog/post-detail.html')