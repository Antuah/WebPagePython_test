from django import forms  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  
from .models import CustomUser  
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']

        # widgets = {
        #     'email': forms.EmailInput(
        #     attrs={
        #         'class': 'form-control',
        #         'placeholder': 'ejemplo@utez.edu.mx',
        #         'pattern': '[a-z0-9]+@utez\.edu\.mx',
        #         'title': 'Debes usar un correo de la UTEZ',
        #         'required': 'required'
        #     }
        #     ),
        #     'name': forms.TextInput(attrs={
        #     'class': 'form-control',
        #     'placeholder': 'Nombre'
        #     }),
        #     'surname': forms.TextInput(attrs={
        #     'class': 'form-control',
        #     'placeholder': 'Apellido'
        #     }),
        #     'control_number': forms.TextInput(attrs={
        #     'class': 'form-control',
        #     'placeholder': 'Número de Control'
        #     }),
        #     'age': forms.NumberInput(attrs={
        #     'class': 'form-control',
        #     'placeholder': 'Edad'
        #     }),
        #     'tel': forms.TextInput(attrs={
        #     'class': 'form-control',
        #     'placeholder': 'Teléfono',
        #     'pattern': '^\d{10}$',
        #     'title': 'El número de teléfono debe tener 10 dígitos'
        #     }),
        #     'password1': forms.PasswordInput(attrs={
        #     'class': 'form-control',
        #     'pattern':"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
        #     'placeholder': 'Contraseña'
        #     }),
        #     'password2': forms.PasswordInput(attrs={
        #     'class': 'form-control',
        #     'pattern':"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
        #     'placeholder': 'Confirmar Contraseña'
        #     }),
        # }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@utez.edu.mx'):
            raise forms.ValidationError("Debes usar un correo de la UTEZ.")
        return email
    
    def clean_control_number(self):
        control_number = self.cleaned_data.get('control_number')
        if len(control_number) < 8:
            raise forms.ValidationError("El número de control debe tener al menos 8 dígitos.")
        return control_number

    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        if len(tel) < 10:
            raise forms.ValidationError("El número de teléfono debe tener 10 dígitos.")
        return tel
    
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")

        if not any(char.isupper() for char in password1):
            raise forms.ValidationError("La contraseña debe contener al menos una letra mayúscula.")

        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")

        if not any(char in "@$!%*?&" for char in password1):
            raise forms.ValidationError("La contraseña debe contener al menos un carácter especial (@$!%*?&).")

        return password1
    

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return password2  

    
    




class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo Electrónico'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
    )

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise forms.ValidationError("Correo o contraseña incorrectos.")

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError("Esta cuenta está desactivada.")
        