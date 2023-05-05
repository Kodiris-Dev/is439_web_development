from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView

from app_info.forms import BeltForm, CategoryForm, ProfileForm, TagForm
from app_info.models import Profile, Post, Category, Tag, Belt, BeltPromotionPost, Technique


class ProfileList(ListView):
    model = Profile


class ProfileDetail(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        profile = self.get_object()

        posts = profile.posts.all()
        belt = profile.belt
        context['posts'] = posts
        context['belt'] = belt

        return context


class ProfileCreate(CreateView):
    form_class = ProfileForm
    model = Profile


class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        post = self.get_object()

        text = post.text
        image = post.image
        created_at = post.created_at
        updated_at = post.updated_at
        likes = post.likes
        title = post.title
        subtitle = post.subtitle
        profile = post.profile
        categories = post.categories
        tags = post.tags.all()
        comments = post.comments.all()

        context['text'] = text
        context['image'] = image
        context['created_at'] = created_at
        context['updated_at'] = updated_at
        context['likes'] = likes
        context['title'] = title
        context['subtitle'] = subtitle
        context['profile'] = profile
        context['categories'] = categories
        context['tags'] = tags
        context['comments'] = comments

        return context


class CategoryList(ListView):
    model = Category


class CategoryDetail(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        category = self.get_object()

        posts = category.posts.all()
        name = category.name

        context['posts'] = posts
        context['name'] = name

        return context


class CategoryCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CategoryForm
    model = Category
    permission_required = ''


class TagList(ListView):
    model = Tag


class TagDetail(DetailView):
    model = Tag

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        tag = self.get_object()

        posts = Post.objects.filter(tags__tag_id=tag.tag_id)
        name = tag.name

        context['posts'] = posts
        context['name'] = name

        return context


class TagCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = TagForm
    model = Tag
    permission_required = ''


class BeltList(ListView):
    model = Belt


class BeltDetail(DetailView):
    model = Belt

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        belt = self.get_object()

        profiles = belt.profiles.all()
        name = belt.name

        context['profiles'] = profiles
        context['name'] = name

        return context


class BeltCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = BeltForm
    model = Belt
    permission_required = ''


class BeltPromotionPostList(ListView):
    model = BeltPromotionPost


class BeltPromotionPostDetail(DetailView):
    model = BeltPromotionPost

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        belt_promotion_post = self.get_object()

        text = belt_promotion_post.text
        image = belt_promotion_post.image
        created_at = belt_promotion_post.created_at
        updated_at = belt_promotion_post.updated_at
        likes = belt_promotion_post.likes
        profile = belt_promotion_post.profile
        belt = belt_promotion_post.belt

        context['text'] = text
        context['image'] = image
        context['created_at'] = created_at
        context['updated_at'] = updated_at
        context['likes'] = likes
        context['profile'] = profile
        context['belt'] = belt

        return context


class TechniqueList(ListView):
    model = Technique


class TechniqueDetail(DetailView):
    model = Technique

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        technique = self.get_object()

        name = technique.name
        tag = technique.tag
        description = technique.description
        link = technique.instructional_link

        context['tag'] = tag
        context['name'] = name
        context['description'] = description
        context['link'] = link

        return context
