# imports
import nltk
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.data.path.append(r"C:\Users\alves\OneDrive\Documentos\datas") # caminho pros .csv    
# configurações iniciais
stopwords = set(stopwords.words("Portuguese"))
stemmer = PorterStemmer()    
# respostas de inicio e fim
respostas = {
    "inicio":["Olá tudo bem?","Eae meu nobre, como vai?"],
    "fim":["Tchau!","Flw!"]
}
def mensagens_possiveis(mensagem):
   tokens = word_tokenize(mensagem.lower())
   tokens = [stemmer.stem(word) for word in tokens if word not in stopwords]
   
   if any(word in tokens for word in ["eae", "oi", "olá"]): 
       return respostas["inicio"] 
   elif any(word in tokens for word in ["flw", "tchau"]):
       return respostas["fim"] 
   else: 
       return ["Resposta indefinida"]