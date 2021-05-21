from community.models import Review, Comment
from movies.models import Movie
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm, CommentForm
from django.http.response import JsonResponse

# Create your views here.
@login_required
@require_http_methods(['GET', 'POST'])
def create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect('movies:detail', movie_pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    comment_form = CommentForm()
    comments = review.comment_set.all() 
    context = {
        'comments': comments,
        'comment_form':  comment_form,
        'review': review,
    }
    return render(request, 'community/detail.html', context)

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
        return redirect('community:detail', review.pk)
    return redirect('accounts:login')



def like(request, pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=pk)
        user = request.user
        # 좋아요 취소
        if review.like_user.filter(pk=user.pk).exist():
            review.like_user.remove(user)
            liked = False
        # 좋아요
        else:
            review.like_user.add(user)
            liked = True

        like_status = {
            'liked' : liked,
            'count' : review.like_user.count(),
        }
        return JsonResponse(like_status)
    # 로그인 되지 않은 경우
    return redirect('accounts:login')
