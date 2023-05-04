from django.views.generic import ListView, DetailView

from app_info.models import Profile, Post, Category


class ProfileList(ListView):
    model = Profile


class ProfileDetail(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        profile = self.get_object()

        posts = profile.posts.all()
        belt = profile.belt_color
        context['posts'] = posts
        context['belt'] = belt

        return context


class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        post = self.get_object()

        # text = models.TextField()
        # image = models.ImageField(default="")
        # created_at = models.DateTimeField(auto_now_add=True)
        # updated_at = models.DateTimeField(auto_now=True)
        # likes = models.IntegerField()
        # title = models.CharField(max_length=45)
        # subtitle = models.CharField(max_length=45)
        # profile = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)
        # categories = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
        # tags = models.ManyToManyField(Tag)
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