from django.shortcuts import render , HttpResponseRedirect
import nltk
nltk.download('wordnet')
nltk.download('punkt')
from nltk.corpus import wordnet


from .form import Word_form , Sentence_form

import nltk 

from nltk.tokenize import word_tokenize, sent_tokenize 

import time

from textblob import TextBlob

parts_of_speech = {
    'CC':"Coordinating Conjunction" , "CD":"Cardinal Digit","DT":"Determiner", "EX":"Existial There",
    "FW":"Foreign Word" , "IN":"Preposition","JJ":"Adjective","JJR":"Adjective(larger)" , "JJS":"Adjective(largest)",
    "LS":"List MArket" , "MD":"Modal","NN":"Noun" , "NNS":"Noun Plural","NNP":"Proper Noun,Singular", "NNPS":"Proper Noun Prural",
    "PDT":"Predeterminer","POS":"Possessive Ending","PRP":"Personal Pronoun","PRP$":"Possessive Pronoun","RB":"Adverb",
    "RBR":"Adverb , Comparative" , "RBS":"Adverb , Superlative","RP":"Particle","TO":"Infinite Maker",
    "UH":"Interjection","VB":"Verb","VBH":"Verb Gerund","VBD":"Verb Past Tense","VBN":"Verb Past Participle",
    "VBP":"Verb ,Present Tense not 3rd person" , "VBZ":"Verb ,Present Tense with 3rd person" , "WDT":"Wh-determiner","WP":"Wh-Pronoun",
    "WRB":"Wh-Adverb"
}
stop_word=(',' ,'.', '!','?','&','#','@','`','(',')','*','+','^','%')

# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = Word_form(data=request.POST)
        if fm.is_valid():
            
            word = fm.cleaned_data['word']
            pre = word
            y = ""
            
            if 'meaning' in request.POST:
                y = "Meaning ->"
                word = meaning(word) 
            if 'synonyms' in request.POST:
                y = "Synonyms ->"
                word = list(synonyms(word))
                

            if 'antonyms' in request.POST:
                y = "Antonyms ->"
                word = antonyms(word)
                if word != "Not Found :(":
                    word = list(word)

            if 'make_sen' in request.POST:
                y = " -> "
                
                word = make_sen(word)  
                print(word)   


                    
            fm = Word_form()

            return render(request , 'words/home.html' , {'form':fm , 'word':word , 'y':str(y) , 'pre':pre})   
        else:
            return HttpResponseRedirect('/') 
    else: 
        fm = Word_form()                              
        return render(request , 'words/home.html' , {'form':fm})


def pos_trans(request):
    
    if request.method == 'POST':
        fm = Sentence_form(data = request.POST)
        if fm.is_valid():
            word = fm.cleaned_data['sentence']
            pre=word
            if 'hindi' in request.POST:
                y =" In Hindi -> "
                word  = translate(word)
            if 'english' in request.POST:
                y = " In Eng -> "
                word = translate_eng(word) 
            if 'pos' in request.POST:
                y = " All Parts Of Speach -> "
                word = pos(word)  
                pre=" "
            fm = Sentence_form()
            
            return render(request , 'words/pos_trans.html' , {'form':fm , 'word':word , 'y':str(y) , 'pre':pre})    
        else:
            return HttpResponseRedirect('/')  
    else:  
        fm = Sentence_form()
        return render(request , 'words/pos_trans.html' , {'form':fm})


def pos(sen):
    tokenized = sent_tokenize(sen)

    for i in tokenized:
        word_list = word_tokenize(i)
        wordlist = [w for w in word_list if not w in stop_word] 
        tagged = nltk.pos_tag(wordlist) 

        my_word =[]
        for i , val in tagged:
            my_word.append((i , parts_of_speech[val]))

    return my_word        
    
    


def translate_eng(sen):
    try:
        word = TextBlob(sen)
        word = word.translate(from_lang='hi' , to = 'en')
    except:
        word = "Don't Know :("
    return word 

def translate(sen):
    try:
        word = TextBlob(sen)
        word = word.translate(from_lang='en' , to = 'hi')
        # print(word)
    except:
        word = "पता नहीं :("
    return word        

def meaning(word):
    # print(word)
    try:
        syns = wordnet.synsets(str(word))
        word = syns[0].definition()
        print(syns[0].lemmas()[0].name())
       
    except:
        word = "Not Found :("    
    
    return word

def synonyms(word):
    # print(word)
    pre = word
    try:
        # print(syns)
        word = []
        for syn in wordnet.synsets(pre):
            for i in syn.lemmas():
                word.append(i.name())
                # print(i.name())
        word = set(word)
        # print(word)
       
        return word
        
    except Exception as e:
        print(e)
        word = "Not Found :("
        return word
                
    

def antonyms(word):
    pre = word
    try:
        word = []
        for syn in wordnet.synsets(pre):
            for i in syn.lemmas():
                # print(i.antonyms())
                if len(i.antonyms())!= 0 :
                    word.append(i.antonyms()[0].name())
                # word.append(i.antonyms()[0].name())
        word = set(word)        
        return word

    except Exception as e:
        print(e)
        word = "Not Found :("
        return word    

def make_sen(word):
    pre = word
    # print(pre)
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
            print(syn1[index].examples())
            word = (syn1[index].examples())[0] 
            print(word)
        else:
            word = "Not Found :("      
        return word   
    except Exception as e:
        print(e)
        word = "Not Found :("
        return word          
      



    

