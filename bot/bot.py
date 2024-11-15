# imports
import os
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Configurações Iniciais
dados_pasta = 'dados'
arquivosCSV = [arquivo for arquivo in os.listdir(dados_pasta) if arquivo.endswith('.csv')]
stopwords = set(stopwords.words("Portuguese"))
stemmer = PorterStemmer()    

# Leitura de Dados
df = pd.DataFrame()
for arquivo in arquivosCSV:
    caminho = os.path.join(dados_pasta,arquivo)
    df = pd.concat([df, pd.read_csv(caminho, encoding="latin-1",delimiter=';',on_bad_lines='skip')], ignore_index=True)

# Reposta
Bases_Conversa = {
    "inicio":["Oi!","Olá!"],
    "fim":["Tchau!"]
}

# Função para identificar as palavras!
def identificarIntencao(tokens):
    intencao = {
        "saudação":["eae","opa","oi","olá"],
        "despedida":["tchau","flw"]
    }
    for intencao, palavra_chave in intencao.items():
        if any(palavra in tokens for palavra in palavra_chave):
            return Bases_Conversa.get(intencao, "salve")
        if palavra_chave == "tchau" or "flw":
            return Bases_Conversa.get(intencao, "Foi um prazer conversar com você :)")

# Função para enviar as mensagens
def Enviomensagens(mensagem):
    tokens = word_tokenize(mensagem.lower())
    tokens = [stemmer.stem(word) for word in tokens if word not in stopwords]
    resposta = identificarIntencao(tokens)
    return print(resposta)

while True:
    mensagem = input("Input: ")
    Enviomensagens(mensagem)
    if any(word in mensagem.lower() for word in ["tchau", "flw"]):
        break