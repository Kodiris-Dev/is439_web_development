from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class BeltColor(models.Model):
    belt_color_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        ordering = ['name']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_id = models.AutoField(primary_key=True)
    displayName = models.CharField(max_length=45, default="")
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    join_date = models.DateTimeField(default=timezone.now)
    profile_picture = models.ImageField(default="")
    banner_picture = models.ImageField(default="")
    belt_color = models.ForeignKey(BeltColor, related_name='profiles', on_delete=models.PROTECT)

    def __str__(self):
        return '%s, %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('app_info_profile_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['first_name']


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        ordering = ['name']


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % (self.name)

    # def get_absolute_url(self):
    #     return reverse('app_info_category_detail_urlpattern',
    #                    kwargs={'pk': self.pk}
    #                    )

    class Meta:
        ordering = ['name']


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    text = models.TextField()
    image = models.ImageField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField()
    title = models.CharField(max_length=45)
    subtitle = models.CharField(max_length=45)
    profile = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return '%s, %s' % (self.title, self.subtitle)

    # def get_absolute_url(self):
    #     return reverse('app_info_post_detail_urlpattern',
    #                    kwargs={'pk': self.pk}
    #                    )

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

#
# class PostTag(models.Model):
#     tag = models.ForeignKey(Tag, related_name='postTags', on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, related_name='postTags', on_delete=models.CASCADE)



