from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class PollForm(forms.Form):
    question = forms.CharField(
        label='Question',
        max_length=100
    )

    choice1 = forms.CharField(
        label='Choice',
        max_length=100
    )

    choice2 = forms.CharField(
        label='Choice',
        max_length=100
    )

    choice3 = forms.CharField(
        label='Choice',
        max_length=100,
        required=False
    )

    choice4 = forms.CharField(
        label='Choice',
        max_length=100,
        required=False
    )
