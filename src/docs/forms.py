from django import forms
from .models import Document

class SearchForm(forms.Form):
    q = forms.CharField(max_length=100)

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=1024, required=True, widget=forms.Textarea)

    def clean_comment(self):
        text = self.cleaned_data['comment']
        if text.isspace():
            raise forms.ValidationError(u'Empty string!')
        return text

class DocumentCreateForm(forms.ModelForm):
    model = Document
    fields = ['title', 'file', 'description', ]