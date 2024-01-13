from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from django import forms

from apps.house.models import Apartment, Contact


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['title', 'description', 'room', 'area', 'floor', 'parking', 'lift', 'stair', 'thumbnail',
                  'division', 'district', 'thana', 'union', 'address', 'image_1', 'image_2', 'image_3', 'rent', 'owner',
                  'is_rent_complete']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['area'].label = 'Area (ft2)'

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None

        self.helper = FormHelper()
        # self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-4 mb-0'),
                Column('rent', css_class='form-group col-md-2 mb-0'),
                Column('area', css_class='form-group col-md-2 mb-0'),
                Column('floor', css_class='form-group col-md-2 mb-0'),
                Column('room', css_class='form-group col-md-2 mb-0'),
            ),
            Row(
                Column('owner', css_class='form-group col-md-6 mb-0'),
                Column('is_rent_complete', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('division', css_class='form-group col-md-3 mb-0'),
                Column('district', css_class='form-group col-md-3 mb-0'),
                Column('thana', css_class='form-group col-md-3 mb-0'),
                Column('union', css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('parking', css_class='form-group col-md-3 mb-0'),
                Column('lift', css_class='form-group col-md-3 mb-0'),
                Column('stair', css_class='form-group col-md-3 mb-0'),
            ),
            Row(
                Column('address', css_class='form-group col-md-6 mb-0'),
                Column('thumbnail', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('image_1', css_class='form-group col-md-4 mb-0'),
                Column('image_2', css_class='form-group col-md-4 mb-0'),
                Column('image_3', css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('description', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column(
                    Submit('submit', 'Create Projects')
                )
            )
        )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None

        self.helper = FormHelper()
        # self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-12 mb-0'),
                Column('phone', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('message', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column(
                    Submit('submit', 'Create Projects')
                )
            )
        )


class ApartmentFiltersForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.layout = Layout(
            Row(
                Column('room', css_class='form-group col-md-1 mb-0'),
                Column('floor', css_class='form-group col-md-1 mb-0'),
                Column('parking', css_class='form-group col-md-1 mb-0'),
                Column('lift', css_class='form-group col-md-1 mb-0'),
                Column('union', css_class='form-group col-md-2 mb-0'),
                Column('rent', css_class='form-group col-md-2 mb-0'),
                Column(HTML("""<button class="btn btn-lg btn-primary">Filter</button>"""),
                       css_class='form-group col-md-1 p-5 mb-0'),
            ),
        )
