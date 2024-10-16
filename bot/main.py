#  imports a serem usados
import re
import nltk

class bot:
    texto = 'Um exemplo bem simples, mas que vai me ajudar eventualmente'
    par = nltk.word_tokenize(texto)
    print(par)
    
class usuario:
    user_name = input('Digite como você deve ser chamado(a): ')
    while True:
        user_chat = input()
        if user_chat == 'sair':
            break