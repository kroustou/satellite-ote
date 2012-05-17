from django.forms import ModelForm
from models import Participation

class RegistrationForm(ModelForm):

    class Meta:
        model = Participation
