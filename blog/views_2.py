from django.shortcuts import render

# Create your views here.

# A function for the starting page:
def start_page(request):
    return render(request, 'blog/index.html')  # The request HAS to be passed to the render() function as well
    """
    render():
    Return a HttpResponse whose content is filled with the result of calling
    django.template.loader.render_to_string() with the passed arguments.
    """


# A function for all the posts:
def posts(request):
    pass


# A function for the individual posts:
def individual_posts(request):
    pass