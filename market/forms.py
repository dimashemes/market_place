from django import forms
from multiupload.fields import MultiFileField
from market.models import ProductImages, Product


class ProductImagesForm(forms.ModelForm):
    class Meta:
        model = ProductImages
        fields = ['image']


class ProductForm(forms.ModelForm):
    # images = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}), required=False)
    images = MultiFileField(min_num=1, max_num=10, required = False)  # Настройте параметры, как вам нужно

    class Meta:
        model = Product
        fields = ['images','name', 'description', 'manufacturer', 'warranty', 'price', 'category']
