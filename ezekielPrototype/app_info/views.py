from django.shortcuts import render, get_object_or_404
from django.views import View

from app_info.models import User


class UserList(View):

    def get(self, request):
        return render(
            request,
            'app_info/user_list.html',
            {'user_list': User.objects.all()}
        )


class UserDetail(View):

    def get(self, request, pk):
        user = get_object_or_404(
            User,
            pk=pk
        )
        return render(
            request,
            'app_info/user_detail.html',
            {'user': user}
        )
