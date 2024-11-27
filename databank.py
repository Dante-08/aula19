import sqlite3

conexecao = sqlite3.connect('meu_banco_de_dados.db')

cursor = conexecao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas(id INTEGER PRMARY KEY
AUTOINCREMENT NOT NULL,
               nome TEXT NOT NULL,
               idade INTEGER NOT NULL,
               cidade TEXT NOT NULL
    )           
''')

# inserir dados na tabela

nome = input('Digite um nome')
idade = int(input('Digite sua idade'))
cidade = input('Cidade: ')
cursor.execute('''
INSERT INTO pessoas (nome, idade, cidade)
VALUES (?, ?, ?)
''', (nome,idade,cidade))

# confirmar transação

conexecao.commit()

cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()

for pessoas in pessoas:
    print(f'''ID: {pessoas[0]}, NOME: {pessoas[1]}, IDADE: {pessoas[2]}, CIDADE: {pessoas[3]}''')

conexecao.close()