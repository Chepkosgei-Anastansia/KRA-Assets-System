from django import forms


class AssetCreation(forms.Form):
    serial_number = forms.CharField(label='First name', max_length=100)
    asset_type= forms.CharField(label='Last Name', max_length=100)
    model_type = forms.EmailField(label='Email Address', max_length=100)
    model_number = forms.CharField(label='User Role', widget=forms.Select(choices= ROLE))
    macs_address =
    2086