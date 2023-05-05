from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Belt(models.Model):
    belt_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % (self.name)

    def get_absolute_url(self):
        return reverse('app_info_belt_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )


    class Meta:
        ordering = ['name']


class Profile(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    join_date = models.DateTimeField(default=timezone.now)
    profile_picture = models.ImageField(default="")
    banner_picture = models.ImageField(default="")
    belt = models.ForeignKey(Belt, related_name='profiles', on_delete=models.PROTECT)

    def __str__(self):
        return '%s, %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('app_info_profile_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('app_info_profile_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    # def get_delete_url(self):
    #     return reverse('app_info_profile_delete_urlpattern',
    #                    kwargs={'pk': self.pk}
    #                    )

    class Meta:
        ordering = ['first_name']


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % (self.name)

    def get_absolute_url(self):
        return reverse('app_info_tag_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['name']


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % (self.name)

    def get_absolute_url(self):
        return reverse('app_info_categories_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['name']


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    text = models.TextField()
    image = models.ImageField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    title = models.CharField(max_length=45)
    subtitle = models.CharField(max_length=45)
    profile = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return '%s, %s' % (self.title, self.subtitle)

    def get_absolute_url(self):
        return reverse('app_info_post_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['title']


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    text = models.TextField(default='')
    profile = models.ForeignKey(Profile, related_name='comments', on_delete=models.PROTECT)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.PROTECT)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % (self.text)

    class Meta:
        ordering = ['text']


class BeltPromotionPost(models.Model):
    belt_promotion_post_id = models.AutoField(primary_key=True)
    text = models.TextField()
    image = models.ImageField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile, related_name='belt_promotion_posts', on_delete=models.CASCADE)
    belt = models.ForeignKey(Belt, related_name="belt_promotion_posts", on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.profile, self.belt)

    def get_absolute_url(self):
        return reverse('app_info_belt_promotion_post_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['belt']


class Technique(models.Model):
    technique_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.TextField(default='')
    instructional_link = models.URLField()
    tag = models.ForeignKey(Tag, related_name='techniques', on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % (self.name)

    def get_absolute_url(self):
        return reverse('app_info_technique_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['name']

