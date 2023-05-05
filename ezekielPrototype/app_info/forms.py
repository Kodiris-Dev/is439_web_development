from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from app_info.models import Profile, Belt, Category, Tag, BeltPromotionPost, Technique, Post, Comment


class BeltForm(ModelForm):
    class Meta:
        model = Belt
        fields = '__all__'

        def clean_name(self):
            return self.cleaned_data['name'].strip()


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        def clean_name(self):
            return self.cleaned_data['name'].strip()


class ProfileForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('join_date', 'last_login', 'groups', 'user_permissions', 'password', 'is_superuser', 'is_staff', 'is_active', 'date_joined')

        def clean_username(self):
            return self.cleaned_data['username'].strip()

        def clean_first_name(self):
            return self.cleaned_data['first_name'].strip()

        def clean_last_name(self):
            return self.cleaned_data['last_name'].strip()


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

        def clean_name(self):
            return self.cleaned_data['name'].strip()


class BeltPromotionPostForm(ModelForm):
    class Meta:
        model = BeltPromotionPost
        fields = '__all__'
        exclude = ('created_at', 'updated_at', 'likes', 'profile')

        def clean_text(self):
            return self.cleaned_data['text'].strip()


class TechniqueForm(ModelForm):
    class Meta:
        model = Technique
        fields = '__all__'

        def clean_name(self):
            return self.cleaned_data['name'].strip()

        def clean_description(self):
            return self.cleaned_data['description'].strip()

        def clean_instructional_link(self):
            return self.cleaned_data['instructional_link'].strip()


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('created_at', 'updated_at', 'likes', 'profile')

        def clean_title(self):
            return self.cleaned_data['title'].strip()

        def clean_subtitle(self):
            return self.cleaned_data['subtitle'].strip()

        def clean_text(self):
            return self.cleaned_data['text'].strip()


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        def clean_text(self):
            return self.cleaned_data['text'].strip()

