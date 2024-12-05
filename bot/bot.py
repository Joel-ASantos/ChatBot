import os
import string
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Configurações Iniciais
dados_pasta = 'dados'
arquivosCSV = [arquivo for arquivo in os.listdir(dados_pasta) if arquivo.endswith('.csv')]
stopwords = set(stopwords.words("portuguese"))

# Função para buscar informações nos dados
def buscarInformacoes(mensagem):
    mensagem_lower = mensagem.lower()
    encontrou_arquivo = False

    for arquivo in arquivosCSV:
        caminho = os.path.join(dados_pasta,arquivo)
        
        try:
            df = pd.read_csv(caminho,encoding="latin-1",delimiter=";",on_bad_lines="skip")
            print(df.tail(5))
            encontrou_arquivo = True
        except Exception as e:
            print(f'Erro ao ler o arquivo: {arquivo}: {e}')
    
    if not encontrou_arquivo:
        return "Não encontrei nenhuma inforção salva"
    else:
        return "Visualização Completa"

# Função para identificar as intenções
def identificarIntencao(tokens):
    intencoes = {
        "saudação": ["eae", "opa", "oi", "olá"],
        "despedida": ["tchau", "flw", "até mais", "até logo"],
        "elogio": ["parabéns", "muito bom", "ótimo"],
        "buscar": ["info", "informação", "dados"],
        "gratidão": ["obrigado", "vlw"],
        "ajuda": ["comandos", "ajuda"]
    }

    respostas = {
        "saudação": "Olá, como posso ajudar?",
        "despedida": "Foi um prazer conversar com você.",
        "elogio": "Muito obrigado! :)",
        "gratidão": "De nada :)",
        "ajuda": (
            "Lista de Comandos:\n"
            "Ao digitar 'info','informação'ou 'dados', será retornado algumas informações da pasta dados\n"
            "Para finalizar a conversa com o bot, digitar 'flw', 'tchau', 'até mais' ou 'até logo'."
        )
    }

    tokens = [token.lower().strip(string.punctuation) for token in tokens]
    for chave, palavras_chave in intencoes.items():
        if any(palavra in " ".join(tokens) for palavra in palavras_chave):
            if chave == "buscar":
                return buscarInformacoes(" ".join(tokens))
            return respostas.get(chave)
    return "Não Entendi"

# Função para tokenização e identificação de intenção
def Tokenizacao_mensagem(mensagem):
    tokens = word_tokenize(mensagem.lower())
    resposta = identificarIntencao(tokens)
    return print(f"Chatbot: {resposta}\n")

# Loop de interação com o chatbot
while True:
    mensagem = input("Input: ")
    Tokenizacao_mensagem(mensagem)
    if any(word in mensagem.lower() for word in ["tchau", "flw","até mais", "até logo"]):
        break