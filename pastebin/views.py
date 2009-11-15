from django import forms
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from pastebin.models import CodePaste



def index(request):
    if request.method == 'POST':
        form = PasteForm(request.POST)
        if form.is_valid():
            paste = form.save()
            request.session['language'] = form.cleaned_data['language']
            request.session['name'] = form.cleaned_data['name']
            return HttpResponseRedirect(paste.get_absolute_url())            
    if request.method == 'GET':
        try:
            language = request.session['language']
            name = request.session['name']
        except KeyError, e:
            language = ''
            name =  ''
        form = PasteForm(initial={'name':name, 'language':language})
    payload = {'form':form}
    return render_to_response('djpaste/create.html', payload, RequestContext(request))

def paste_details(request, id):
    paste = get_object_or_404(CodePaste, id = id)
    payload = {'paste':paste}
    return render_to_response('djpaste/details.html', payload, RequestContext(request))

def plain(request, id):
    paste = get_object_or_404(CodePaste, id = id)
    return HttpResponse(paste.text, mimetype="text/plain")

def html(request, id):
    paste = get_object_or_404(CodePaste, id = id)
    return HttpResponse(paste.htmld_text, mimetype="text/plain")

class PasteForm(forms.Form):
    lang_names = (('Python', 'Python', ), ('Perl', 'Perl',), ('Ruby', 'Ruby',), ('PythonConsole', 'Python Console'), \
        ('RubyConsole', 'Ruby Console'), ('PythonTraceback', 'Python Traceback'), ('HtmlDjango','Django Template'),\
        ('Html', 'Html'), ('Others', 'Others'))
    text = forms.CharField(label='Code', widget=forms.Textarea(attrs = {"rows":20, "cols":80}))
    language = forms.ChoiceField(lang_names, required = False)
    title = forms.CharField(required = False, max_length=60, widget = forms.TextInput(attrs = {'size':50}))
    name = forms.CharField( max_length=60, widget = forms.TextInput(attrs = {'size':50}), required = False)
    def save(self):
        snippet = CodePaste(text = self.cleaned_data['text'], language=self.cleaned_data['language'], title=self.cleaned_data['title'], name=self.cleaned_data['name'])
        snippet.save()
        return snippet