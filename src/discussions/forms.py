from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(max_length=100)

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=1024, required=True, widget=forms.Textarea)

    def clean_comment(self):
        text = self.cleaned_data['comment']
        if text.isspace():
            raise forms.ValidationError(u'Empty string!')
        return text