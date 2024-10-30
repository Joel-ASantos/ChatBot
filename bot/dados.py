# imports
import nltk
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class Bot:
    def dados():
        nltk.data.path.append(r"C:\Users\alves\OneDrive\Documentos\datas") # caminho pros .csv
    
    def mensagens_possiveis():
        print
        