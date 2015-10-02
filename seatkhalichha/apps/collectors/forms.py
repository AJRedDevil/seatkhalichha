from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from apps.collectors.models import Collector_Contents
from apps.carpools.models import VEHICLE_TYPE


class FeedViewForm(forms.ModelForm):
    """
    A form that displays a third party feed data
    """

    content = forms.CharField(widget=forms.Textarea())

    pickup_time = forms.DateTimeField(
        error_messages={
            'required': 'Approximate pickup time is required !',
        })

    occupancy = forms.IntegerField(
        error_messages={
            'required': 'No of seats available is required !',
        })

    vehicle_type = forms.ChoiceField(
        choices=VEHICLE_TYPE,
        error_messages={
            'required': 'Vehicle required!',
            'invalid_choice': 'Please select one of the options available !',
        },
    )

    route = forms.CharField(
        error_messages={
            'required': 'Approximate pickup time is required !',
        })

    remarks = forms.CharField(required=False)

    class Meta:
        model = Collector_Contents
        fields = ['content']


    def __init__(self, *args, **kwargs):
        super(FeedViewForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs={'class' : 'form-control', 'rows': 8}
        self.fields['pickup_time'].widget.attrs={'class' : 'form-control dateTimePicker'}
        self.fields['pickup_time'].input_formats=['%Y/%m/%d %H:%M']
        self.fields['occupancy'].widget.attrs={'class' : 'form-control'}
        # self.fields['end_datetime'].widget.attrs={'class' : 'form-control dateTimePicker', 'placeholder': '2015/09/30 18:00', 'readonly': 'readonly'}
        # self.fields['end_datetime'].input_formats=['%Y/%m/%d %H:%M']
        self.fields['route'].widget.attrs.update({'class' : 'form-control'})
        self.fields['remarks'].widget.attrs={'class' : 'form-control', 'placeholder': 'Anything you want to say to the rider. '}


