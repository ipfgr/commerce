from django import forms
class AddNewItemForm(forms.Form):
    name = forms.CharField(label='Product name', max_length=64)
    productImage = forms.URLField(label='Please add url to image', required=True)
    quantity = forms.IntegerField(label="Quantity of product")
    aboutProduct = forms.CharField(label='About', required=True, help_text="Add information about product", widget=forms.Textarea)


class CommentsForm(forms.Form):
    name= forms.CharField(label="Name", max_length=64)
    commenttext = forms.CharField(label="Comment", max_length=300, widget=forms.TextInput(attrs={

    }))


