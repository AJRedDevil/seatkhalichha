from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Carpools, Carpool_Requests

class MinLengthValidator(validators.MinLengthValidator):
    message = 'Ensure this value has at least %(limit_value)d elements (it has %(show_value)d).'


class MaxLengthValidator(validators.MaxLengthValidator):
    message = 'Ensure this value has at most %(limit_value)d elements (it has %(show_value)d).'


class CommaSeparatedCharField(forms.Field):
    def __init__(self, dedup=True, max_length=None, min_length=None, *args, **kwargs):
        self.dedup, self.max_length, self.min_length = dedup, max_length, min_length
        super(CommaSeparatedCharField, self).__init__(*args, **kwargs)
        if min_length is not None:
            self.validators.append(MinLengthValidator(min_length))
        if max_length is not None:
            self.validators.append(MaxLengthValidator(max_length))

    def to_python(self, value):
        if value in validators.EMPTY_VALUES:
            return []

        value = [item.strip() for item in value.split(',') if item.strip()]
        if self.dedup:
            value = list(set(value))

        return value

    def clean(self, value):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)
        return value


class CommaSeparatedIntegerField(forms.Field):
    default_error_messages = {
        'invalid': 'Enter comma separated numbers only.',
    }

    def __init__(self, dedup=True, max_length=None, min_length=None, *args, **kwargs):
        self.dedup, self.max_length, self.min_length = dedup, max_length, min_length
        super(CommaSeparatedIntegerField, self).__init__(*args, **kwargs)
        if min_length is not None:
            self.validators.append(MinLengthValidator(min_length))
        if max_length is not None:
            self.validators.append(MaxLengthValidator(max_length))

    def to_python(self, value):
        if value in validators.EMPTY_VALUES:
            return []

        try:
            value = [int(item.strip()) for item in value.split(',') if item.strip()]
            if self.dedup:
                value = list(set(value))
        except (ValueError, TypeError):
            raise ValidationError(self.error_messages['invalid'])

        return value

    def clean(self, value):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)
        return value


class CarpoolCreationForm(forms.ModelForm):
    """
    A form that creates a post, from the given data
    """

    # route = CommaSeparatedCharField(
    #     label=_("route"),
    #     help_text=_("Enter a comma separated list of landmarks!"),
    #     error_messages={
    #         'required': 'Please provide with a route !',
    #     })

    class Meta:
        model = Carpools
        fields = ['vehicle_type', 'start_datetime', 'end_datetime', 'remarks', 'route', 'occupancy', ]

    def __init__(self, *args, **kwargs):
        super(CarpoolCreationForm, self).__init__(*args, **kwargs)
        self.fields['vehicle_type'].widget.attrs={'class' : 'form-control'}
        self.fields['start_datetime'].widget.attrs={'class' : 'form-control dateTimePicker', }
        self.fields['start_datetime'].input_formats=['%Y/%m/%d %H:%M']
        self.fields['end_datetime'].widget.attrs={'class' : 'form-control dateTimePicker', 'placeholder': '2015/09/30 18:00'}
        self.fields['end_datetime'].input_formats=['%Y/%m/%d %H:%M']
        self.fields['remarks'].widget.attrs={'class' : 'form-control', 'placeholder': 'Smoking not allowed OR only ladies passengers!'}
        self.fields['occupancy'].widget.attrs={'class' : 'form-control'}
        self.fields['route'].widget.attrs={'class' : 'form-control', 'placeholder': 'Budhanilkantha to Baluwatar'}


class CarpoolEditForm(forms.ModelForm):
    """
    A form that edits a carpool data
    """

    class Meta:
        model = Carpools
        fields = ['vehicle_type', 'remarks', 'occupancy', 'start_datetime', 'end_datetime']


    def __init__(self, *args, **kwargs):
        super(CarpoolEditForm, self).__init__(*args, **kwargs)
        self.fields['vehicle_type'].widget.attrs.update({'class' : 'form-control'})
        self.fields['remarks'].widget.attrs={'class' : 'form-control', 'placeholder': 'Smoking not allowed OR only ladies passengers!'}
        self.fields['occupancy'].widget.attrs.update({'class' : 'form-control'})
        self.fields['start_datetime'].widget.attrs={'class' : 'form-control dateTimePicker'}
        self.fields['start_datetime'].input_formats=['%Y-%m-%d %H:%M', '%Y-%m-%d %H:%M:%S', '%Y/%m/%d %H:%M']
        self.fields['end_datetime'].widget.attrs={'class' : 'form-control dateTimePicker', 'placeholder': '2015/09/30 18:00'}
        self.fields['end_datetime'].input_formats=['%Y-%m-%d %H:%M', '%Y-%m-%d %H:%M:%S', '%Y/%m/%d %H:%M']


class CarpoolViewForm(forms.ModelForm):
    """
    A form that displays a carpool data
    """

    class Meta:
        model = Carpools
        fields = ['vehicle_type', 'remarks', 'occupancy', 'start_datetime', 'end_datetime']


    def __init__(self, *args, **kwargs):
        super(CarpoolViewForm, self).__init__(*args, **kwargs)
        self.fields['vehicle_type'].widget.attrs={'class' : 'form-control'}
        self.fields['start_datetime'].widget.attrs={'class' : 'form-control dateTimePicker', }
        self.fields['start_datetime'].input_formats=['%Y/%m/%d %H:%M']
        self.fields['end_datetime'].widget.attrs={'class' : 'form-control dateTimePicker', 'placeholder': '2015/09/30 18:00'}
        self.fields['end_datetime'].input_formats=['%Y/%m/%d %H:%M']
        self.fields['remarks'].widget.attrs={'class' : 'form-control', 'placeholder': 'Smoking not allowed OR only ladies passengers!'}
        self.fields['occupancy'].widget.attrs={'class' : 'form-control'}

class CarpoolRequestCreateForm(forms.ModelForm):
    """
    A form that edits a carpool data
    """

    class Meta:
        model = Carpool_Requests
        fields = ['message']

    def __init__(self, *args, **kwargs):
        super(CarpoolRequestCreateForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'class' : 'form-control', 'placeholder':'I need to be at my school. I can come to Chakrapath at 9!'})
