from .models import Word , Sentence
from django import forms

class Word_form(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word']
        labels={'word':'Word'}
        widgets = {
            'word':forms.TextInput(attrs={'class':"form-control" , 'placeholder':"Single Word"})
        }


class Sentence_form(forms.ModelForm):
    class Meta:
        model = Sentence
        fields = ['sentence']
        labels={'sentence':'Sentence'}
        widgets={
            'sentence':forms.TextInput(attrs={'class':"form-control" , 'placeholder':'Sentence'})
        }
        

        
