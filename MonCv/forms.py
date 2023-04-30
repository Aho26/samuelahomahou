from django.forms import ModelForm
from MonCv.models import Message

class MessageForms(ModelForm):
    class Meta :
        model= Message
        fields='__all__'