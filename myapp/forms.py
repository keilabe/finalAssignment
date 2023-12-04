from django import forms
from myapp.models import Destinations, Holidayreserve, ContactMessage


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destinations
        fields = ['Image', 'dname', 'eprice', 'description', 'country']


class Holidayreserveform(forms.ModelForm):
    class Meta:
        model = Holidayreserve
        fields = ['firstname', 'lastname', 'email', 'telephone', 'startDate', 'endDate', 'no_of_adults',
                  'no_of_children', 'destination', 'total_amount']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
<<<<<<< HEAD
=======

#
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['text']
>>>>>>> 6fc92ba (My Bootcamp-SP project)
