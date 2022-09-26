from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import resolve
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile
from posts.models import Post


class ProfileView(LoginRequiredMixin, View):
    model = Profile
    template_name = 'profile.html'

    def get(self, request, **kwargs):
        profile = get_object_or_404(self.model, user=self.request.user)
        url_name = resolve(self.request.path).url_name

        if url_name == 'profile':
            posts = Post.objects.filter(user=self.request.user)
        else:
            posts = profile.favorites.all()

        page_number = request.GET.get('page')
        paginator = Paginator(posts, 2)
        try:
            page = paginator.get_page(page_number)
        except PageNotAnInteger:
            page = paginator.get_page(1)
        except EmptyPage:
            pass

        context = {
            'posts': page,
            'profile': profile
        }
        return render(self.request, self.template_name, context)


