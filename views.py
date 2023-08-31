from utils import load_data, load_template, build_response, adiciona
from urllib.parse import unquote_plus
from database import Database, Note

def index(request):
    db = Database('data/banco')

    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[-1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        if corpo != "":
            chave_valor = corpo.split('&')
            esquerda = chave_valor[0].split("=")
            titulo = unquote_plus(esquerda[1])
            direita = chave_valor[1].split("=")
            conteudo = unquote_plus(direita[1])
            params[titulo] = conteudo
        
        db.add(Note(title=titulo, content=params[titulo]))

        return build_response(code=303, reason='See Other', headers='Location: /')

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    
    
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content)
        for dados in load_data(db)
    ]
        
    notes = '\n'.join(notes_li)

    body = load_template('index.html').format(notes=notes)

    return build_response(body = body)