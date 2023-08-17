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
    
def adiciona(anotacao):
    with open("data/notes.json", 'w') as arquivo:
        lista = load_data("notes.json")
        lista.append(anotacao)
        novo_json = json.dumps(lista)
        return arquivo.write(novo_json)
    
def build_response(body='', code=200, reason='OK', headers=''):
    response = ''
    if headers == '':
        response = "HTTP/1.1 " + str(code) + " " + reason + headers + "\n\n" + body
    else:
        response = "HTTP/1.1 " + str(code) + " " + reason + "\n" + headers + "\n\n" + body
    return str(response).encode()