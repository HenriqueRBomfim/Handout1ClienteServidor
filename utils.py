import json
from database import Database, Note

def extract_route(requisicao):
    return requisicao.split(" ")[1][1:]

def read_file(path):
    with open(path, 'rb') as f:
        return f.read()

def load_data(db):
    '''with open("data/" + nome, 'r', encoding='utf-8') as arquivo_json:
        texto = arquivo_json.read()
    return json.loads(texto)'''
    return db.get_all()

def load_template(arquivo):
    with open("templates/" + arquivo, 'r', encoding='utf-8') as string:
        return string.read()
    
def adiciona(anotacao):
    lista = load_data("notes.json")
    lista.append(anotacao)
    with open("data/notes.json", 'w', encoding='utf-8') as arquivo:
        return arquivo.write(json.dumps(lista, indent=4))
    
def build_response(body='', code=200, reason='OK', headers=''):
    response = ''
    if headers == '':
        response = "HTTP/1.1 " + str(code) + " " + reason + headers + "\n\n" + body
    else:
        response = "HTTP/1.1 " + str(code) + " " + reason + "\n" + headers + "\n\n" + body
    return str(response).encode()