#  imports a serem usados
import nltk
from nltk.corpus import movie_reviews

# fill up bot with data
nltk.data.path.append("C:\\Users\\alves\\OneDrive\\Documentos\\datas")
    
class usuario:
    user_name = input('Digite como você deve ser chamado(a): ')
    while True:
        user_chat = input()
        if user_chat == 'sair':
            break