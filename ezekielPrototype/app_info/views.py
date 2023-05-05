from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin, UpdateView

from app_info.forms import BeltForm, CategoryForm, ProfileForm, TagForm, BeltPromotionPostForm, TechniqueForm, PostForm, \
    CommentForm
from app_info.models import Profile, Post, Category, Tag, Belt, BeltPromotionPost, Technique, Comment


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

    def form_valid(self, form):
        valid = super(ProfileCreate, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


class ProfileUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ProfileForm
    model = Profile
    template_name = 'app_info/profile_form_update.html'
    permission_required = ''

    def form_valid(self, form):
        valid = super(ProfileUpdate, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


class PostList(ListView):
    model = Post


class PostDetail(FormMixin, DetailView):
    model = Post
    form_class = CommentForm
    # template_name = 'app_info/comment_form_update.html'


    def get_success_url(self):
        return reverse_lazy('app_info_post_detail_urlpattern', kwargs={'pk': self.object.pk})

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

        context['form'] = self.get_form()
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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post = self.get_object()
        form.instance.profile = self.request.user
        form.save()
        return super().form_valid(form)


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    permission_required = ''

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'app_info/post_form_update.html'
    permission_required = ''


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


class CategoryUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CategoryForm
    model = Category
    template_name = 'app_info/category_form_update.html'
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


class TagUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = TagForm
    model = Tag
    template_name = 'app_info/tag_form_update.html'
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


class BeltUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = BeltForm
    model = Belt
    template_name = 'app_info/belt_form_update.html'
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


class BeltPromotionPostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = BeltPromotionPostForm
    model = BeltPromotionPost
    permission_required = ''


class BeltPromotionPostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = BeltPromotionPostForm
    model = BeltPromotionPost
    template_name = 'app_info/beltpromotionpost_form_update.html'
    permission_required = ''


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


class TechniqueCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = TechniqueForm
    model = Technique
    permission_required = ''


class TechniqueUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = TechniqueForm
    model = Technique
    template_name = 'app_info/technique_form_update.html'
    permission_required = ''


# class CommentUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
#     form_class = CommentForm
#     model = Comment
#     template_name = 'app_info/comment_form_update.html'
#     permission_required = ''
#
#     def get_success_url(self):
#         return reverse_lazy('app_info_post_detail_urlpattern', kwargs={'pk': self.})
