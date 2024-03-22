from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post, Purchase, Style,Review
from .forms import ReviewForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 3


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    reviews = post.reviews.all().order_by("-date_review")
    reviews_count = post.reviews.filter(approved=True).count()

    purchases= post.purchases.all()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review= review_form.save(commit=False)
            review.author_review = request.user
            review.post_review = post
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval!'
    )
    
    review_form = ReviewForm()




    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
        "reviews": reviews,
        "reviews_count": reviews_count,
        "purchases": purchases,
        "review_form": review_form,
        },
    )

