from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms

from apps.house.models import Apartment


class MyApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['title', 'description', 'room', 'area', 'floor', 'parking', 'lift', 'stair', 'thumbnail',
                  'division', 'district', 'thana', 'union', 'address', 'image_1', 'image_2', 'image_3', 'rent',
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
                Column('is_rent_complete', css_class='form-group col-md-2 mb-0'),
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
