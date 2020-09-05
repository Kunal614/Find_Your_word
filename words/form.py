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
        labels={'sentence':'Max 300 words Sentence'}
        # sentence= forms.CharField(widget=forms.Textarea(attrs={"rows":1, "cols":1}))
        widgets = {
          'sentence': forms.Textarea(attrs={'rows':8, 'cols':25}),
        }
        

        
