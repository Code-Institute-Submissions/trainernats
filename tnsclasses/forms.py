from django import forms
from .models import TNS_Class, Day


class TNS_ClassForm(forms.ModelForm):

    class Meta:
        model = TNS_Class
        fields = '__all__'
        image = forms.ImageField(label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        day = Day.objects.all()
        friendly_names = [
                          (d.id, d.get_friendly_name()) for d in day
                         ]
        self.fields['day'].choices = friendly_names
        self.fields['class_time'].widget.attrs[
                                               'placeholder'
                                               ] = 'Enter time (hh:mm)'
        self.fields['class_name'].widget.attrs[
                                               'placeholder'
                                               ] = 'Enter class name'
        self.fields['class_description'].widget.attrs[
                            'placeholder'
                            ] = 'Enter a brief class description - displayed in the classes summary'
        self.fields['class_more_detail'].widget.attrs[
                                                      'placeholder'
                                                      ] = 'Enter a full description of the class - displayed on the class details page'
        self.fields['price'].widget.attrs[
                                          'placeholder'
                                          ] = 'Enter price to 2 decimal places'
        self.fields['image_url'].widget.attrs[
                                              'placeholder'
                                              ] = 'Enter an image URL'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'mb-2'
