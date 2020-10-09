from django import forms
from .models import BlogPost
from django.core import validators
from .models import RegisterUser

class postDate(forms.ModelForm, forms.Form):
    findingBot= forms.CharField(widget=forms.HiddenInput, required=False)
    postImage= forms.ImageField(required=False)
    class Meta:
        model = BlogPost
        fields = "__all__"
        exclude = ['postDate','postID']

        labels = {
            'postHeader': "Post Head",
            "postData ": "Post Content",
            "postImage": "Post Poster"
        }
        widgets = {
            'postHeader': forms.TextInput(attrs={'class': "form-control"}),
            'postData': forms.Textarea(attrs={'class': "form-control",}),
            'postAdmin' : forms.HiddenInput()

        }

    def clean_findingBot(self):
        value= self.cleaned_data['findingBot']
        if len(value) >0:
             raise forms.ValidationError('You are a Bot.')
        return value

class Signin(forms.Form):

    email= forms.CharField(required=True, error_messages={'required': "Email is required"},
                widget=forms.EmailInput(attrs={"placeholder": 'Email'}))

    password= forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": 'Password'}),
                              required=True, error_messages={'required': "Password is Required!"},)


class Registration(forms.ModelForm):
    email= forms.CharField(widget=forms.EmailInput(attrs={"placeholder": 'Email'}), required=True,
                           error_messages={'required': "Email is required!"})
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": 'First Name'}), required=True,
                               error_messages={'required': "First Name is required!"})
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": 'Last Name'}), required=True,
                               error_messages={'required': "Last Name is required!"})

    password= forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": 'Password'}), required=True,
                              error_messages={'required': "Password is required!"})

    repassword= forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": 'Confirm Password'}), required=True,
                              error_messages={'required': "Password is required!"} )

    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     confPassword= self.cleaned_data.get('repassword')
    #
    #     if password != confPassword:
    #         raise forms.ValidationError('Password does not match.')
    #
    #     return password

    def clean(self):
        cleandata= super(Registration, self).clean()
        password= cleandata.get('password')
        repassword= cleandata.get('repassword')

        if password != repassword:
            self.add_error('password','Password does not match.')

    class Meta:
        model= RegisterUser
        fields= ['email', 'password', 'first_name', 'last_name']


class resetPassword(forms.Form):
    email= forms.CharField(widget=forms.EmailInput)

    def clean(self):
        data= super(resetPassword, self).clean()
        email= RegisterUser.objects.filter(email=data.get('email')).first()
        if email is None:
            self.add_error('email', 'This user does not exist.')