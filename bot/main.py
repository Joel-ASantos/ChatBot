#  imports a serem usados
import nltk
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
    
class Bot:
    userChat = input()
    
    def processamentos_mensagens(userChat):
        print()