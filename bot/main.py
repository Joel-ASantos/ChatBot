#  imports a serem usados
import nltk

class NTKL:
    nltk.download('all')

user_name = input('Digite como você deve ser chamado(a): ')

while True:
    user_chat = input()
    if user_chat == 'sair':
        break