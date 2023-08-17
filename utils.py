import json

def extract_route(requisicao):
    return requisicao.split(" ")[1][1:]

def read_file(path):
    with open(path, 'rb') as f:
        resposta = f.read()
    return resposta

def load_data(nome):
    with open("data/" + nome, 'r') as arquivo_json:
        texto = arquivo_json.read()
    return json.loads(texto)

def load_template(arquivo):
    with open("templates/" + arquivo, 'r') as string:
        return string.read()