from django import forms
from .models import TNS_Class, Day, Class_Type


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
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 mb-2'
