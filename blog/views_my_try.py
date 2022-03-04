from datetime import date
from django.shortcuts import render

# Each post will be a dictionary:
posts = [
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

# Trying it by myself first. See it in the file python_test_3.py in python_test_project
# folder
"""
def get_date(a_list: list, users_key) -> dict.values:
    a_list_2 = []
    global item_value
    for item in a_list:
        for key in item.keys():
            item_value = item[users_key]
        a_list_2.append(item_value)
    return sorted(a_list_2)


print(get_date(posts, 'date'))
result_get_date = get_date(posts, 'date')[-1]
print(result_get_date)


def start_page_3(chosen_list, dict_key):
    result = get_date(chosen_list, dict_key)[-1]
    return result


print(start_page_3(posts, 'date'))
"""


def get_date(post: dict):
    return post['date']  # Since post is a dictionary, we want to return this dictionary's values
    # Another option:
    # return post.get('date')
    """
    Code that I wrote:
    for post in posts:
        date_value = post["date"]
    return date_value
    """


"""
for post in posts:
    my_value = post["date"]
"""


# A function for the starting page:
def start_page(request):
    sorted_posts = posts.sort(key=get_date)  # We don't need to write get_date() with the
    # parentheses because we don't want Python to execute the function. Instead we just point
    # at get_date
    length_sorted_posts = len(sorted_posts)
    latest_posts = sorted_posts[::-length_sorted_posts]
    return render(request, 'blog/index.html')


# A function for all the posts:
def posts(request):
    return render(request, 'blog/all_posts.html')


# A function for the individual posts:
def individual_posts(request, slug):
    return render(request, 'blog/post-detail.html')