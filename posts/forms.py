from django import forms
from .models import Post
from .models import Tag


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


TAG_CHOICES= [(i.name, i.name) for i in Tag.objects.all()]

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'contact-input',
            'placeholder': 'Enter Username',
        }
    ))
    email = forms.EmailField(label='Enter email', widget=forms.EmailInput(
        attrs={
            'class': 'contact-input',
            'placeholder': 'Enter Email',
        }
    ))

    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(
        attrs={
            'class': 'contact-input',
            'placeholder': 'Enter Password'
        }
    ))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={
            'class': 'contact-input',
            'placeholder': 'Confirm Password'
        }
    ))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        # if r.count():
        #     raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        user.save()
        return user


class CustomUserLoginForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'contact-input',
            'placeholder': 'Enter Username',
        }
    ))

    password = forms.CharField(label='Enter password', widget=forms.PasswordInput(
        attrs={
            'class': 'contact-input',
            'placeholder': 'Enter Password'
        }
    ))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')

        # if password1 and password2 and password1 != password2:
        #     raise ValidationError("Password don't match")

        return password

    # def save(self, commit=True):
    #     user = User.objects.create_user(
    #         self.cleaned_data['username'],
    #         self.cleaned_data['email'],
    #         self.cleaned_data['password1']
    #     )
    #    return user


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'contact-input',
            'placeholder': 'Title',
        }
    ))

    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'contact-textarea',
            'placeholder': 'Description',
        }
    ))

    tag = forms.CharField(label='Select tag', widget=forms.Select(choices=TAG_CHOICES,
        attrs={
            'class': 'contact-input',
            'placeholder': 'Select Tag'
        }
    ))

    image = forms.CharField(widget=forms.FileInput(
        attrs={
            'class': 'form-control-file',
        }
    ))

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'tag',
            'image',
        ]
