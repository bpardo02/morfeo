from django import forms
from .models import Sueno

class SuenoForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)
    class Meta:
        model = Sueno
        fields = ["iniciales", "titulo", "mensaje"]


    def clean_iniciales(self):
        iniciales = self.cleaned_data.get("iniciales", "").strip().upper() # convertir a mayúsculas y eliminar espacios
        if len(iniciales) != 3:
            raise forms.ValidationError("Debe ingresar exactamente 3 iniciales.")
        return iniciales

    def clean_descripcion(self):
        texto = self.cleaned_data.get("mensaje", "")

        # evitar descripciones vacías o muy cortas
        if len(texto.strip()) < 10:
            raise forms.ValidationError("El sueño debe tener al menos 10 caracteres.")
        
        return texto

    def clean_honeypot(self):
        valor = self.cleaned_data.get("honeypot")
        if valor:  # si alguien llenó este campo, es bot
            raise forms.ValidationError("No eres humano 👀")
        return valor