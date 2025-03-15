from django import forms

class BulkEmailForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    recipient_list = forms.CharField(
        widget=forms.Textarea,
        help_text="Enter multiple emails separated by commas"
    )
