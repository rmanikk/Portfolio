from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):

    class Meta:
        model = ContactMessage

        fields = [
            "name",
            "email",
            "subject",
            "message",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your name",
                    "autocomplete": "name",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "your@email.com",
                    "autocomplete": "email",
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "placeholder": "What's this about?",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "placeholder": "Tell me about your project...",
                    "rows": 6,
                }
            ),
        }