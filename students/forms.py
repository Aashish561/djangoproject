from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Student

class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'department', 'address', 'email', 'phone']
    
    def __init__(self, *args, **kwargs):
        self.admin = kwargs.pop('admin', None)
        super().__init__(*args, **kwargs)
        if self.admin:
            self.fields['department'].initial = self.admin.department
            self.fields['department'].disabled = True