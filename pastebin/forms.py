from django import forms
from .models import CodePaste


class PasteForm(forms.Form):
    lang_names = (('Python', 'Python',), ('Perl', 'Perl',), 
        ('Ruby', 'Ruby',), ('PythonConsole', 'Python Console'),
        ('RubyConsole', 'Ruby Console'),
        ('PythonTraceback', 'Python Traceback'),
        ('HtmlDjango', 'Django Template'),
        ('Html', 'Html'), ('Others', 'Others'))
    text = forms.CharField(label='Code', 
                            widget=forms.Textarea(attrs={"rows": 20, "cols": 80}))
    language = forms.ChoiceField(lang_names, required=False)
    title = forms.CharField(required=False, max_length=60, 
                            widget=forms.TextInput(attrs={'size': 50}))
    name = forms.CharField(max_length=60, 
                            widget=forms.TextInput(attrs={'size': 50}), required=False)
    
    def save(self):
        snippet = CodePaste(text=self.cleaned_data['text'], 
                            language=self.cleaned_data['language'], 
                            title=self.cleaned_data['title'], 
                            name=self.cleaned_data['name'])
        snippet.save()
        return snippet
        
