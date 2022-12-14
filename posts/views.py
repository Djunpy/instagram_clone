from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView

from .models import Post, Tag, Stream
from .forms import CreatePostForm

class HomePageView(LoginRequiredMixin, View):

    template_name = 'home-page.html'
    model = Post

    def get(self, *args, **kwargs):
        context = {
            'object_list': self.get_queryset()
        }
        return render(self.request, self.template_name, context)

    def get_queryset(self):
        stream_post_ids = Stream.objects.filter(user=self.request.user).values_list('post_id', flat=True)
        queryset = self.model.objects.select_related('user').filter(id__in=stream_post_ids).order_by('-created')
        return queryset

class CreatePostView(LoginRequiredMixin, View):
    model = Post
    form_class = CreatePostForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST or None, self.request.FILES or None)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            description = form.cleaned_data.get('description')
            tags = form.cleaned_data.get('tags')

            tag_list = []
            for tag in tags.split(','):
                t, created = Tag.objects.get_or_create(title=tag)
                tag_list.append(t)

            new_post = Post.objects.create(
                user=self.request.user,
                picture=picture,
                description=description
            )
            new_post.tags.set(tag_list)
            new_post.save()
            return redirect('/')
        else:
            self.form_class(self.request.POST or None, self.request.FILES or None)


class ByTag(ListView):
    model = Post
    template_name = ''

    def get_queryset(self):
        queryset = Post.objects\
            .select_related('user')\
            .prefetch_related('tags')\
            .filter(tags__slug=self.kwargs['slug'])
        return queryset

