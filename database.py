import sqlite3
from dataclasses import dataclass
class Database():
    def __init__(self, nome):
        self.conn = sqlite3.connect(nome + '.db')
        self.conn.execute("CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);")

    def add(self, note):
        texto = "INSERT INTO note (title,content) VALUES (? , ?);"
        valores = (note.title, note.content)
        self.conn.execute(texto, valores)
        self.conn.commit()
    
    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        lista = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            note = Note(id,title,content)
            lista.append(note)
        return lista
    
    def update(self, entry):
        cursor = self.conn.cursor()
        comando = "UPDATE note SET title = ?, content = ? WHERE id = ?"
        cursor.execute(comando, (entry.title, entry.content, entry.id))
        self.conn.commit()

    def delete(self, note_id):
        cursor = self.conn.cursor()
        comando = "DELETE FROM note WHERE id = ?"
        cursor.execute(comando, (note_id,))
        self.conn.commit()

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

    
