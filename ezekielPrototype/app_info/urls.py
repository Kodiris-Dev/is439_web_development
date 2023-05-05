"""ezekielPrototype URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app_info.views import ProfileList, ProfileDetail, PostList, PostDetail, CategoryList, CategoryDetail, TagList, \
    TagDetail, BeltList, BeltDetail, BeltPromotionPostList, BeltPromotionPostDetail, TechniqueList, TechniqueDetail, \
    BeltCreate, CategoryCreate, ProfileCreate, TagCreate

urlpatterns = [
    path('profiles/',
         ProfileList.as_view(),
         name='app_info_profile_list_urlpattern'),
    path('profiles/<int:pk>/',
         ProfileDetail.as_view(),
         name='app_info_profile_detail_urlpattern'),
    path('profiles/create/',
         ProfileCreate.as_view(),
         name='app_info_profile_create_urlpattern'),
    path('all_posts/',
         PostList.as_view(),
         name='app_info_post_list_urlpattern'),
    path('posts/<int:pk>/',
         PostDetail.as_view(),
         name='app_info_post_detail_urlpattern'),
    path('categories/',
         CategoryList.as_view(),
         name='app_info_categories_list_urlpattern'),
    path('categories/<int:pk>/',
         CategoryDetail.as_view(),
         name='app_info_categories_detail_urlpattern'),
    path('categories/create/',
         CategoryCreate.as_view(),
         name='app_info_category_create_urlpattern'),
    path('tags/',
         TagList.as_view(),
         name='app_info_tag_list_urlpattern'),
    path('tags/<int:pk>/',
         TagDetail.as_view(),
         name='app_info_tag_detail_urlpattern'),
    path('tags/create/',
         TagCreate.as_view(),
         name='app_info_tag_create_urlpattern'),
    path('belts/',
         BeltList.as_view(),
         name='app_info_belt_list_urlpattern'),
    path('belts/<int:pk>/',
         BeltDetail.as_view(),
         name='app_info_belt_detail_urlpattern'),
    path('belts/create/',
         BeltCreate.as_view(),
         name='app_info_belt_create_urlpattern'),
    path('belt_promotions/',
         BeltPromotionPostList.as_view(),
         name='app_info_belt_promotion_post_list_urlpattern'),
    path('belt_promotions/<int:pk>/',
         BeltPromotionPostDetail.as_view(),
         name='app_info_belt_promotion_post_detail_urlpattern'),
    path('techniques/',
         TechniqueList.as_view(),
         name='app_info_technique_list_urlpattern'),
    path('techniques/<int:pk>/',
         TechniqueDetail.as_view(),
         name='app_info_technique_detail_urlpattern'),
]
