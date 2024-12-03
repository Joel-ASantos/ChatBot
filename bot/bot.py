import os
import string
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Configurações Iniciais
dados_pasta = 'dados'
arquivosCSV = [arquivo for arquivo in os.listdir(dados_pasta) if arquivo.endswith('.csv')]
stopwords = set(stopwords.words("portuguese"))

# Leitura de Dados
df = pd.DataFrame()
for arquivo in arquivosCSV:
    caminho = os.path.join(dados_pasta, arquivo)
    df = pd.concat([df, pd.read_csv(caminho, encoding="latin-1", delimiter=';', on_bad_lines='skip')], ignore_index=True)

# Função para identificar as intenções
def identificarIntencao(tokens):
    intencoes = {
        "saudação": ["eae", "opa", "oi", "olá"],
        "despedida": ["tchau", "flw", "até mais", "até logo"],
        "elogio": ["parabéns", "muito bom", "ótimo"]
    }

    respostas = {
        "saudação": "Olá, como posso ajudar?",
        "despedida": "Foi um prazer conversar com você.",
        "elogio": "Muito obrigado! :)"
    }

    tokens = [token.lower().strip(string.punctuation) for token in tokens]
    for chave, palavras_chave in intencoes.items():
        if any(palavra in " ".join(tokens) for palavra in palavras_chave):
            return respostas.get(chave)
    return "Não Entendi"

# Função para tokenização e identificação de intenção
def Tokenizacao_mensagem(mensagem):
    tokens = word_tokenize(mensagem.lower())
    resposta = identificarIntencao(tokens)
    return print(f"Chatbot: {resposta}")

# Loop de interação com o chatbot
while True:
    mensagem = input("Input: ")
    Tokenizacao_mensagem(mensagem)
    if any(word in mensagem.lower() for word in ["tchau", "flw"]):
        break