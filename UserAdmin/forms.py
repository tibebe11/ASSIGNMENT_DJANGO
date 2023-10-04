from django import forms
from django.contrib.auth.forms import UserCreationForm
from Account.models import CustomUser
from Company.models import Blog, Blog_Categories
from froala_editor.widgets import FroalaEditor

class SuperUserCreationForm(UserCreationForm):
    class Meta: 
        model: CustomUser
        fields = ('first_name','last_name', 'username', 'email','password1', 'password2')

        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'last_name' : forms.TextInput(attrs={
                'class' : 'form=control'
            }),
            'username' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control'
            }),
            'password1' : forms.PasswordInput(attrs={
                'class':'form-control'
            }),
            'password2' : forms.PasswordInput(attrs={
                'class' : 'form-control'
            })
        }


class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields =('title', 'image', 'description', 'content', 'type')

        widgets  = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'image' : forms.ClearableFileInput(attrs={
                'class' : 'form-control'
            }),
            'description' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'content' : FroalaEditor,
            'type' : forms.SelectMultiple(attrs={
                'class' : 'form-select'
            })
        }



