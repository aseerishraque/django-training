from django import forms
from blog.views import Post

class PostForm(forms.ModelForm):
    # title = forms.CharField(max_length=500)
    # body = forms.CharField(widget=forms.Textarea, required=False)
    # status = forms.CharField(max_length=20, required=False)
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ('title', 'body', 'status', 'author')
