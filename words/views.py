from django.shortcuts import render , HttpResponseRedirect

from .form import Word_form

# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = Word_form(data=request.POST)
        if fm.is_valid():
            # inp = fm.cleaned_data['Meaning']
            word = fm.cleaned_data['word']
            pre = word
            y = ""
            if 'meaning' in request.POST:
                y = "Meaning"
                word = meaning(word) 
            if 'synonyms' in request.POST:
                y = "Synonyms"
                word = Synonyms(word)

            if 'antonyms' in request.POST:
                y = "Antonyms"
                word = Antonyms(word)

            if 'make_sen' in request.POST:
                y = "Make Sentence"
                word = Make_sen(word)        
                    
            fm = Word_form()

            return render(request , 'words/home.html' , {'form':fm , 'word':word , 'y':y , 'pre':pre})   
        else:
            return HttpResponseRedirect('/') 
    else: 
        fm = Word_form()                              
        return render(request , 'words/home.html' , {'form':fm})

def meaning(word):
    word = "kunal"
    return word

def Synonyms(word):
    word = "kunal"
    return word

def Antonyms(word):
    word = "kunal"
    return word

def Make_sen(word):
    word = "kunal"
    return word    



    

