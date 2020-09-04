from django.shortcuts import render , HttpResponseRedirect

from nltk.corpus import wordnet

from .form import Word_form , Sentence_form

import time

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
                y = "Meaning ->"
                word = meaning(word) 
            if 'synonyms' in request.POST:
                y = "Synonyms ->"
                word = list(Synonyms(word))
                

            if 'antonyms' in request.POST:
                y = "Antonyms ->"
                word = Antonyms(word)
                if word != "Not Found :(":
                    word = list(word)

            if 'make_sen' in request.POST:
                y = " -> "
                
                word = Make_sen(word)  
                print(word)      
                    
            fm = Word_form()

            return render(request , 'words/home.html' , {'form':fm , 'word':word , 'y':str(y) , 'pre':pre})   
        else:
            return HttpResponseRedirect('/') 
    else: 
        fm = Word_form()                              
        return render(request , 'words/home.html' , {'form':fm})


def pos_trans(request):
    fm = Sentence_form()
    return render(request , 'words/pos_trans.html' , {'form':fm})
    

def meaning(word):
    print(word)
    try:
        syns = wordnet.synsets(str(word))
        word = syns[0].definition()
        print(syns[0].lemmas()[0].name())
    except:
        word = "Not Found :("    
    
    return word

def Synonyms(word):
    # print(word)
    pre = word
    try:
        # syns = wordnet.synsets(str(word))
        # print(syns)
        word = []
        for syn in wordnet.synsets(pre):
            for i in syn.lemmas():
                word.append(i.name())
                # print(i.name())
        word = set(word)
        print(word)
       
        return word
        
    except Exception as e:
        print(e)
        word = "Not Found :("
        return word
                
    

def Antonyms(word):
    pre = word
    try:
        word = []
        for syn in wordnet.synsets(pre):
            for i in syn.lemmas():
                print(i.antonyms())
                if len(i.antonyms())!= 0 :
                    word.append(i.antonyms()[0].name())
                # word.append(i.antonyms()[0].name())
        word = set(word)        
        return word

    except Exception as e:
        print(e)
        word = "Not Found :("
        return word    

def Make_sen(word):
    pre = word
    print(pre)
    try:
        syn1 = wordnet.synsets(pre)
        print(syn1)
        flag=0
        index =-1
        for syn in wordnet.synsets(pre):
            for cnt , i in enumerate(syn.lemmas()):
                if pre == i.name():
                    index = cnt
                    flag=1
                    break
            if flag == 1:
                break

        if index!= -1:        
            print(index)  
            word = (syn1[index].examples())[0] 
            print(word)
        else:
            word = "Not Found :("      
        return word   
    except Exception as e:
        print(e)
        word = "Not Found :("
        return word          
      



    

