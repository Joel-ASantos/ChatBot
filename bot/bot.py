# imports
import os
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Configurações Iniciais
dados_pasta = "dados"
arquivosCSV = [arquivo for arquivo in os.listdir(dados_pasta) if arquivo.endswith('.csv')]
stopwords = set(stopwords.words("Portuguese"))
stemmer = PorterStemmer()    

# Leitura de Dados
df = pd.DataFrame()
for arquivo in arquivosCSV:
    caminho = os.path.join(dados_pasta,arquivo)
    df = df.append(pd.read_csv(caminho), ignore_index=True)

# Reposta
dicio = {}

# Função para as mensagens
def mensagens(mensagem):
    tokens = word_tokenize(mensagem.lower())
    tokens = [stemmer.stem(word) for word in tokens if word not in stopwords]