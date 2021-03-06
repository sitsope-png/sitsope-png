from django import forms
from youtubeapp.models import Entry, Language
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Utilisateur(UserCreationForm):
    class Meta:
        model= User
        fields=['username', 'email', 'password1', 'password2']


class EntryCreationForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['language'].queryset = Language.objects.none()

        if 'language' in self.data:
            self.fields['language'].queryset = Language.objects.all()
            #print(self.fields['language'].queryset)

        elif self.instance.pk:
            self.fields['language'].queryset = Language.objects.all().filter(pk=self.instance.language.pk)


from django import forms
class contactformemail(forms.Form):
    Email=forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


subscription_options = [
    ('1-Day subscription', '$1 USD/Day'),
    ('1-Month subscription', '$10 USD/Month'),
]



class SubscriptionForm(forms.Form):
    plans = forms.ChoiceField(choices=subscription_options)


