from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', widget=forms.TextInput(attrs={'placeholder': 'Enter a food item'}))
