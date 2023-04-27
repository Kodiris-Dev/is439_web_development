from django.views.generic import ListView, DetailView

from app_info.models import Profile, Post


class ProfileList(ListView):
    model = Profile


class ProfileDetail(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        profile = self.get_object()

        posts = profile.posts.all()
        context['posts'] = posts

        return context
