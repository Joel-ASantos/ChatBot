# imports
import os
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

def interacoes():
    print()

# Função para identificar as palavras!
def identificarIntencao(tokens):
    intencoes = {
        "saudação": ["eae", "opa", "oi", "olá"],
        "despedida": ["tchau", "flw"]
    }

    Bases_Conversa_bot = {
        "saudação": ["Salve","Olá!","Eae","Opa"],
        "despedida": ["Foi um prazer conversar com você :)","Tchau!"]
    }

    for chave, palavras_chave in intencoes.items():
        if any(palavra in tokens for palavra in palavras_chave):
            return Bases_Conversa_bot.get(chave)
    return "Não Entendi"
    
# Função para tokenização e para impressão da resposta do bot
def Tokenizacao_mensagem(mensagem):
    tokens = word_tokenize(mensagem.lower())
    tokens = [stemmer.stem(word) for word in tokens if word not in stopwords]
    resposta = identificarIntencao(tokens)
    return print(resposta)

while True:
    mensagem = input("Input: ")
    Tokenizacao_mensagem(mensagem)
    if any(word in mensagem.lower() for word in ["tchau", "flw"]):
        break