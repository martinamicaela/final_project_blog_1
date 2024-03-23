from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Purchase, Style, Review
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

def review_edit(request, slug, review_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author_review == request.user:
            review = review_form.save(commit=False)
            review.post = post
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))