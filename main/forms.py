from django.forms import ModelForm
from django import forms
from main.models import Product

class ProductForm(ModelForm):
    # Define different size choices for different categories
    CLOTHING_SIZE_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'), 
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]
    
    SHOES_SIZE_CHOICES = [
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
    ]
    
    available_sizes = forms.MultipleChoiceField(
        choices=CLOTHING_SIZE_CHOICES,  # Default to clothing sizes
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Available Sizes"
    )
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'thumbnail', 'category', 'is_featured', 'brand', 'available_sizes']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Get category from initial data or POST data
        category = None
        if 'category' in self.data:
            category = self.data.get('category')
        elif self.instance.pk and self.instance.category:
            category = self.instance.category
            
        # Set size choices based on category
        if category == 'shoes':
            self.fields['available_sizes'].choices = self.SHOES_SIZE_CHOICES
        else:
            self.fields['available_sizes'].choices = self.CLOTHING_SIZE_CHOICES
            
        # Add CSS classes for dynamic behavior
        self.fields['category'].widget.attrs.update({
            'id': 'id_category',
            'onchange': 'updateSizeChoices()'
        })
        
        if self.instance.pk:
            # Jika edit, set initial values dari database
            initial_sizes = self.instance.get_sizes_list()
            self.fields['available_sizes'].initial = initial_sizes
            
    def save(self, commit=True):
        instance = super().save(commit=False)
        # Convert list of sizes to comma-separated string
        sizes_list = self.cleaned_data['available_sizes']
        instance.set_sizes_list(sizes_list)
        if commit:
            instance.save()
        return instance