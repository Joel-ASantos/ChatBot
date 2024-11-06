#  imports a serem usados
import nltk
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from dados import mensagens_possiveis

userChat = input("envie uma mensagem: ")
envioMensagens = mensagens_possiveis(userChat)
print(envioMensagens)