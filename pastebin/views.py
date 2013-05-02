from django import forms
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views.generic.base import View

from .forms import PasteForm

from .models import CodePaste


class FormIndex(View):
    form_class = PasteForm
    initial = {'name': 'name', 'language': 'language'}
    template_name = 'djpaste/create.html'
    payload = {'form': 'form'}

    def get(self, request, *args, **kwargs):
        
        try:
            self.initial['language'] = request.session['language']
            self.initial['name'] = request.session['name']
        except KeyError, e:
            self.initial['language'] = ''
            self.initial['name'] = ''
        form = self.form_class(initial=self.initial)
        self.payload['form'] = form
        return render_to_response('djpaste/create.html', self.payload, RequestContext(request))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            paste = form.save()
            request.session['language'] = form.cleaned_data['language']
            request.session['name'] = form.cleaned_data['name']
            return HttpResponseRedirect(paste.get_absolute_url())

index = FormIndex.as_view()

class PasteDetails(View):
    def get(self, request, id):
        paste = get_object_or_404(CodePaste, id = id)
        payload = {'paste':paste}
        return render_to_response('djpaste/details.html', payload, RequestContext(request))

paste_details = PasteDetails.as_view()

class Plain(View):
    def get(self, request, id):
        paste = get_object_or_404(CodePaste, id = id)
        return HttpResponse(paste.text, mimetype="text/plain")

plain = Plain.as_view()

class Html(View):
    def get(self, request, id):
        paste = get_object_or_404(CodePaste, id = id)
        return HttpResponse(paste.htmld_text, mimetype= "text/plain")

html = Html.as_view()
