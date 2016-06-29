from django import forms
from spiritbuzz.models import Product, Category, ProductReview





class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = "__all__"

class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the name of the product.")
    description = forms.CharField(max_length=1000, help_text="Please enter a description.")
    size = forms.IntegerField()
    price = forms.DecimalField(help_text = "Please enter sale price:")
    picture = forms.ImageField()


    class Meta:
        # Provide an association between the ModelForm and a model
        model = Product

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        fields = ('name','description', 'size', 'price', 'picture')


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('Price must be greater than 0.')

        return self.cleaned_data['price']

class ProductAddToCartForm(forms.Form):


    quantity = forms.IntegerField(widget = forms.TextInput(attrs = {'size': '2', 'value': '1', 'class': 'quantity', 'maxlength': '5'}), error_messages = {'invalid': 'Please enter a valid quantity.'}, min_value = 1)
    product_slug = forms.CharField(widget = forms.HiddenInput())

    def __init__(self, request = None, *args, **kwargs):
        self.request = request
        super(ProductAddToCartForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError("Cookies must be enabled.")

        return self.cleaned_data

class ProductReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        exclude = ('user', 'product', 'is_approved')