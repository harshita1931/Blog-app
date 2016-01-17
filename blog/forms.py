from django import forms

from .models import Post, Comment

#creating forms

#PostForm is the name of the form
class PostForm(forms.ModelForm):
	#class Meta tells that Post model is used to create this form
    class Meta:
        model = Post
        fields = ('title', 'text',)

#form add comments to posts 
class CommentForm(forms.ModelForm):
	#class Meta tells that Comment model is used to create this form
    class Meta:
        model = Comment
        fields = ('author', 'text',)