import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from django.shortcuts  import redirect
from django.http import HttpResponse
import os

module_dir = os.path.dirname(__file__)  
file_path = os.path.join(module_dir, 'MayaChatbotStrings.txt')
f = open(file_path,'r') 
raw = f.read()
raw = raw.lower()

sent_tokens = nltk.sent_tokenize(raw)

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punc_dict = dict((ord(punct),None) for punct in string.punctuation)
# print(string.punctuation)
# print(remove_punc_dict)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punc_dict)))

GREETING_INPUTS = ['hey','hi','hii','hello','I want your help','hiii','greetings','sup',"what's up",'wassup','bro']

GREETING_RESPONSES = ['hi','hello! How can I help you?','hi ! How can I help you?','hello','welcome ! how can I help you?','hey','hi there','I am glad! You are talking to me.']

def greeting(user_input):
    for word in user_input.split():
        if word in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def get_response(user_response):
    bot_response = ''
    sent_tokens.append(user_response)

    TfidfVec = TfidfVectorizer(tokenizer = LemNormalize)
    # print(TfidfVec)
    tfidf = TfidfVec.fit_transform(sent_tokens)
    # print(tfidf)

    vals = cosine_similarity(tfidf[-1],tfidf)
    # print(vals)
    idx = vals.argsort()[0][-2]
    # print(idx)

    flat = vals.flatten()
    # print(flat)
    flat.sort()
    # print(flat)

    req_tfidf = flat[-2]

    if req_tfidf == 0:
        return bot_response + "Sorry! I don't understand you."
    else:
        return bot_response + sent_tokens[idx]


def MayaResponse(request):
    if request.method == 'POST':
        user_response = request.POST['msg'].lower()
        if user_response in ['bye','byy','meet you soon']:
            return HttpResponse('Bye! Welcome again. Take care ...')
        elif user_response in ['thanks','thank you','thankyou','thanks for help','thank you for your help']:
            return HttpResponse('you are welcome ... Need any more help...')
        if user_response in ['no','noo'] :
            return HttpResponse("Thank you! Welcome again..")
        else:
            if greeting(user_response) != None:
                return HttpResponse( greeting(user_response) )
            else:
                return HttpResponse( get_response(user_response) )
                # sent_tokens.remove(user_response)

    return redirect('/')



# flag = True
# print("Hi! I am Charlie. How can I help you? To exit type'Bye'.")

# while flag:
#     user_response = input('>> ').lower()
#     if user_response in ['bye','byy','meet you soon']:
#         print('Bye! Welcome again. Take care ...')
#         flag = False
#     elif user_response in ['thanks','thank you','thankyou','thanks for help','thank you for your help']:
#         print('you are welcome ... Need any more help...')
#         if input('>> ').lower() in ['no','noo'] :
#             print("Thank you! Welcome again..")
#             flag=False
#     else:
#         if greeting(user_response) != None:
#             print(greeting(user_response))
#         else:
#             print(get_response(user_response))
#             # sent_tokens.remove(user_response)

