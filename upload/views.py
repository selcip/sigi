# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os

# Create your views here.
class HomePageView(TemplateView):
    @method_decorator(login_required)
    def get(self, request, **kwargs):
        return render(request, 'index.html', {'dir': settings.BASE_DIR + settings.MEDIA_ROOT})


def dirlist(request):
    r = ['<ul class="jqueryFileTree" style="display: none;">']
    try:
        r = ['<ul class="jqueryFileTree" style="display: none;">']
        d = request.POST.get('dir', '/tmp')
        for f in os.listdir(d):
            ff = os.path.join(d, f)
            if os.path.isdir(ff):
                r.append(
                    '<li class="directory collapsed"><a href="#" rel="%s/">%s</a></li>' % (ff, f))
            else:
                e = os.path.splitext(f)[1][1:]  # get .ext and remove dot
                r.append(
                    '<li class="file ext_%s"><a href="#" rel="%s">%s</a></li>' % (e, ff, f))
        r.append('</ul>')
    except Exception, e:
        r.append('Could not load directory: %s' % str(e))
    r.append('</ul>')
    return HttpResponse(''.join(r))
