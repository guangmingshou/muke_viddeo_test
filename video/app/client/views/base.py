# coding:utf-8

from django.views.generic import View
from django.shortcuts import reverse, redirect


class Index(View):
    TEMPLATE = 'client/base.html'

    def get(self, request):
        return redirect(reverse('client_ex_video'))