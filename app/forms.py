from django import forms
from .models import Sueno

class SuenoForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Sueno
        fields = ["iniciales", "titulo", "mensaje"]
        widgets = {
            "iniciales": forms.TextInput(
                attrs={
                    "class": "form-input w-full rounded-md border p-3 text-base",
                    "placeholder": "ABC",
                }
            ),
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-input w-full rounded-md border p-3 text-base",
                    "placeholder": "Ej: Soñando con volar",
                }
            ),
            "mensaje": forms.Textarea(
                attrs={
                    "class": "form-input min-h-48 w-full rounded-md border p-3 text-base",
                    "placeholder": "Describe tu sueño con detalle...",
                    "rows": 6,
                }
            ),
        }

    def clean_iniciales(self):
        iniciales = self.cleaned_data.get("iniciales", "").strip().upper()
        if len(iniciales) != 3:
            raise forms.ValidationError("Debe ingresar exactamente 3 iniciales.")
        return iniciales

    def clean_mensaje(self):
        texto = self.cleaned_data.get("mensaje", "")
        if len(texto.strip()) < 10:
            raise forms.ValidationError("El sueño debe tener al menos 10 caracteres.")
        return texto

    def clean_honeypot(self):
        valor = self.cleaned_data.get("honeypot")
        if valor:
            raise forms.ValidationError("No eres humano 👀")
        return valor
