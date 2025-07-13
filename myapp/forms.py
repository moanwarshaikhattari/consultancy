# # myapp/forms.py
# from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Your Name',
#             'required': 'required'
#         })
#     )
#     number = forms.CharField(
#         max_length=10,
#         min_length=10,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Phone No.',
#             'required': 'required',
#             'pattern': '^[0-9]{10}$',
#             'title': 'Enter exactly 10 digits only'
#         })
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Your Email',
#             'required': 'required'
#         })
#     )
#     message = forms.CharField(
#         widget=forms.Textarea(attrs={
#             'class': 'form-control',
#             'placeholder': 'Message',
#             'rows': 4,
#             'required': 'required'
#         })
#     )

   
