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
        diretorio = settings.BASE_DIR + settings.MEDIA_ROOT
        return render(request, 'index.html', {'dir': diretorio})


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
                # do nothing
                e = os.path.splitext(f)[1][1:]  # get .ext and remove dot
                # r.append(
                #     '<li class="file ext_%s"><a href="#" rel="%s">%s</a></li>' % (e, ff, f))
        r.append('</ul>')
    except Exception, e:
        r.append('Could not load directory: %s' % str(e))
    r.append('</ul>')
    return HttpResponse(''.join(r))

def itemlist(request):
    try:
        response = ['']
        d = request.POST.get('dir')
        for f in os.listdir(d):
            ff = os.path.join(d, f)
            if os.path.isdir(ff):
                response.append(
                    '<div class="col-lg-2"><div class="card"><h4 class="card-header">%s</h4></div></div>' % (f)
                )
            else:
                e = os.path.splitext(f)[1][1:]
                response.append(
                    '<div class="col-lg-2"><div class="card"><h4 class="card-header">%s</h4>' % (f)
                )
                response.append(ff)
                response.append(
                    '<div class="card-footer text-muted text-xs-center">%s</div></div></div>' % (e)
                )
    except Exception, e:
        response.append('deu bad')
    return HttpResponse(response)