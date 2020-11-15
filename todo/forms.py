from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from todo.models import TodoList


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['name', 'description', 'date_deadline']
    name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': '해야할일',
            }
        )
    )

    description = forms.CharField(
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'class': 'textarea',
                'placeholder': '할일에 대한 디테일',
            }
        )
    )

    date_deadline = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'id': 'datepicker',
                'placeholder': 'YYYY-MM-DD',
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        date_deadline = cleaned_data.get("date_deadline")

        if date_deadline < datetime.today().date():
            raise ValidationError(
                "데드라인이 잘못되었습니다"
            )
        return cleaned_data
