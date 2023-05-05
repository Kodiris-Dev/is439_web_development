from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from app_info.models import Profile, Belt, Category, Tag


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

        def clean_displayname(self):
            return self.cleaned_data['displayName'].strip()

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


