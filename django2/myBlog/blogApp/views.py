from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

from django import forms
from django.urls import reverse_lazy, reverse

from django.utils import timezone

from django.views.generic import (ListView, TemplateView, CreateView,
                                  View, DeleteView, UpdateView)

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from .models import Post, Category, Comment, Follow
from .forms import PostForm, RegistrationForm, CategoryForm, CommentForm

# Posts from people current user is following.


class IndexPage(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = '/'

    def get(self, request):
        # Where the following person is the current person which is request.user
        user_follows = Follow.objects.filter(user=request.user)

        if request.user.is_authenticated:
            # if request.user follows anyone:
            if user_follows:
                # user follows query set 2
                user_followsqs2 = Follow.objects.filter(
                    user=request.user).all()
                # this query will return a single QuerySet anyway,
                # so i am just getting the first item.
                user_follows2 = user_followsqs2.first().followed_user.all()
                # here we are getting the posts of the followed users.
                # give me posts WHERE the authors are the users in user_follows2 query.
                users_posts = Post.objects.filter(author__in=user_follows2)
                context = {'following_users_posts': users_posts}
                return render(request, 'index.html', context)
        # In the end.
        return render(request, 'index.html')


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'registration.html'
    success_url = reverse_lazy('blogApp:index_page')
    form_class = RegistrationForm
    success_message = 'You have successfully registered.'


class CategoryView(ListView):
    template_name = 'categories.html'
    model = Category
    context_object_name = 'categories'
    # ordering by newest.
    ordering = ['-date']


class PostCommentsView(ListView):
    def get(self, request, pk):
        form = CommentForm()
        # we are getting relevant comments.
        context = {'comments': Comment.objects.filter(post=pk),
                   'post': Post.objects.get(id=pk),
                   'form': form}
        return render(request, 'post_detail.html', context)

    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(id=pk)
        if form.is_valid():
            instance = form.save(commit=False)
            # we are not saving the form right away.
            # instead we are manipulating it.
            # so that we can actually save it in our database.
            instance.author = request.user
            # author of the comment is the current user.
            instance.post = post
            # the post that the comment belongs to.
            form.save()
            # args = (post.id,) that comma at the end is important.
            return redirect(reverse('blogApp:post_detail_page', args=(post.id,)))
        else:
            raise forms.ValidationError('Form is not valid.')
            return redirect(reverse('blogApp:post_detail_page', args=(post.id,)))


class PostUpdate(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = [
        'text'
    ]

    success_url = '/'


def category_detail_view(request, id):
    # Getting the posts of the category that particular category.
    post = Category.objects.get(id=id).post_set.all().filter(
        pub_date__lt=timezone.now()).order_by('-pub_date')
    # in Post table we have
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # so we can get all the posts that are in that category by writing this:
    # Category.objects.get(id=id).post_set.all().
    # post_set.all() gives us all the posts that belong to that particular category.

    post2 = Category.objects.get(id=id)
    context = {'category_posts': post,
               'category_name': post2,
               'form': PostForm()}

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.category = Category.objects.get(id=id)
            form.save()
            return redirect(reverse('blogApp:category_detail_page', args=(id,)))
        else:
            return redirect(reverse('blogApp:category_detail_page', args=(id,)))

    return render(request, 'cat_detail.html', context)


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')

        # built-in authentication
        user = authenticate(username=username, password=password)
        # if user is authenticated:
        if user:
            # built-in login.
            login(request, user)
            return redirect('/')
        else:
            # refreshing the page basically :D
            return redirect('/login')
    # if request.method is not POST:
    return render(request, 'login.html')


@ login_required
def sign_out(request):
    # built-in logout.
    logout(request)
    return redirect('/')


def posts_view(request):
    context = {'form': PostForm}
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = PostForm(data=request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.user_id = request.user.id
                form.save()
        else:
            return redirect('/login')
    else:
        form = PostForm()
    return render(request, 'posts.html', context)


@ login_required
def like(request, pk):
    if request.method == 'POST':
        # post_like_button will give us post.pk value.
        post = get_object_or_404(
            Post, id=request.POST.get('post_like_button'))
        # we are adding request.user to posts' likes.
        post.likes.add(request.user)
        # print(request.get_full_path)
        # print(request.META.get('HTTP_REFERER'))

        # redirect back to the previous page after liking a post
        # in a particular category
        # otherwise, everytime we liked a post in ,say, Web Development
        # category, we would be redirected to the index page everytime

        previous_url = request.META.get('HTTP_REFERER')
        # we are redirecting back the user to the category that he/she was browsing.
        if 'category' in previous_url:
            # hurl --> handle url
            hurl = previous_url.split('/')
            cat_id = hurl[-2]
            return HttpResponseRedirect(reverse_lazy('blogApp:category_detail_page', args=cat_id))
        return HttpResponseRedirect(reverse_lazy('blogApp:index_page'))


def profile_detail_view(request, id):
    # since we have an author column in Post table
    # we can access all the posts that a specific user
    # has.
    user_posts = User.objects.get(id=id).post_set.all().filter(
        pub_date__lt=timezone.now()).order_by('-pub_date')
    user = User.objects.get(id=id)

    # ...qs --> ...query set
    # where the following user object is request.user which is the current user.
    logged_in_user_followsqs = Follow.objects.filter(user=request.user).all()

    # we are getting all the followed users.
    logged_in_user_follows = logged_in_user_followsqs.first(
    ).followed_user.all()

    # initiating an empty array.
    follows = []
    # and filling it up with all the followed users.
    for user in logged_in_user_follows:
        follows.append(user)

    # we are looking at our own profile.
    if request.user == User.objects.get(id=id):
        user_followsqs = Follow.objects.filter(user=id).all()
        user_follows = user_followsqs.first().followed_user.all()

        # if I use user for the value of user context
        # there is a bug which sets your profile as the
        # person you just followed.

        context = {'user_context': User.objects.get(id=id),
                   'user_posts': user_posts,
                   'user_follows': user_follows,
                   'logged_in_user_follows': follows}

    # we are stalking someone else's profile.
    else:
        context = {'user_context': User.objects.get(id=id),
                   'user_posts': user_posts,
                   'logged_in_user_follows': follows}

    return render(request, 'profile.html', context)


def search_topic(request):
    # we are getting the query value.
    query = request.GET.get('q')
    # WHERE icontains %%
    categories = Category.objects.filter(category_name__icontains=query)
    context = {'results': categories,
               'query': query}
    return render(request, 'topicquery.html', context)


def new_topic(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('blogApp:category_page'))
        else:
            return render(request, 'topiccreate.html', {'form': CategoryForm()})
    return render(request, 'topiccreate.html', {'form': CategoryForm()})


def delete_a_post(request, id):
    post = Post.objects.get(id=id)
    user = request.user
    # checking if the it is the author of the post
    # trying to delete a post.
    # we only show delete option to the users' own posts.
    # but there may be some mischievious people who can
    # hardcode, 'delete-post/(id_of_the_post)'.
    if user == post.author:
        post.delete()
        return redirect(reverse('blogApp:profile_detail_page', args=(user.id,)))
    else:
        return render(request, 'delete_error.html')


def follow_user(request, id):
    # well... user to follow.
    user_to_follow = User.objects.get(id=id)
    # current user's follow object.
    follow_object = Follow.objects.get(user=request.user)
    # adding user to follow to follow object of the current user
    # as a followed user.
    follow_object.followed_user.add(id)

    return redirect(reverse('blogApp:profile_detail_page', args=(user_to_follow.id,)))


def unfollow_user(request, id):
    # simple
    unfollow_object = Follow.objects.get(user=request.user)
    unfollow_object.followed_user.remove(id)

    return redirect(reverse('blogApp:profile_detail_page', args=(request.user.id,)))


def search_a_user(request):
    user_query = request.GET.get('userq')
    user_query_context = User.objects.filter(username__icontains=user_query)

    return render(request, 'user_query_results.html', {'user_query_results': user_query_context,
                                                       'query_keyword': user_query})
