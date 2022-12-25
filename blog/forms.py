from django import forms
from .models import Post, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body','slug', 'image',)

    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control', 'id':'title', 'placeholder':'Title of Blog Post'})
        self.fields['body'].widget.attrs.update({'class' : 'form-control', 'id':'body', 'placeholder':'blog post content'})
        self.fields['slug'].widget.attrs.update({'class' : 'form-control', 'id':'body', 'placeholder':'blog post content'})
        self.fields['image'].widget.attrs.update({'class' : 'form-control', 'id':'title', 'placeholder':'Title of Blog Post'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({ 'id':'messages', 'class':'form-control', 'placeholder':'Please Enter Your Comment Here'})


