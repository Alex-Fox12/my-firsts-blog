from django.forms import ModelForm
from .models import Comments, Post

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['com_text', 'ComImage']

class AddPost(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'content', 'post_cat', 'upload', 'AltText']