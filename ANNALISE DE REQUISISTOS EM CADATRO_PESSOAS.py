"""Cadastro simplificado de pessoas usando o banco de dados MySQL """
import mysql.connector 


pessoas=dict()#criado o dicionario que deve receber as variaveis

def conexao():
  conectar=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="cadastro_pessoas")
  cursor = conectar.cursor()
  return conectar,cursor

def criar_tabela(cursor):
  cursor.execute("CREATE DATABASE IF NOT EXISTS cadastro_pessoas")
  cursor.execute("USE cadastro_pessoas")
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS pessoas(
      id_pessoa INT AUTO_INCREMENT NOT NULL,
      nome VARCHAR(50) NOT NULL,
      sexo VARCHAR(2) NOT NULL,
      idade INT NOT NULL,
      PRIMARY KEY (id_pessoa))
  """)
  
def inserir_pessoa(cursor, conectar, pessoa):
  print('inserindo')
  cursor.execute("INSERT INTO pessoas (nome, sexo, idade) VALUES (%s, %s, %s)", 
                  (pessoa['nome'], pessoa['sexo'], pessoa['idade']))
  conectar.commit()
  print('inserido')

def contar_pessoa(cursor):
  cursor.execute("SELECT COUNT(*) FROM pessoas")
  return cursor.fetchone()[0]

def lista_sexo(cursor ,sexo):
  cursor.execute("select nome from pessoas where sexo = %s", (sexo,))
  return cursor.fetchall()

def media_idade(cursor):
  cursor.execute("select avg(idade) from pessoas")
  return cursor.fetchone()[0]

def id_pessoa(cursor, id_pessoa):
  cursor.execute("select * from pessoas where id_pessoa=%s",(id_pessoa,))
  return cursor.fetchone()

def id_por_pessoa():
  while True:
    try:
      pessoa_id = int(input('\n0-Sair\ndigite o ID da pessoa para ver todas as informacoes: '))
      if pessoa_id == 0:
          break
      pessoa = id_pessoa(cursor, pessoa_id)
      if pessoa:
          print(f'\nInformações da pessoa com ID {pessoa_id}:')
          print(f'ID: {pessoa[0]}\nNome: {pessoa[1]}\nSexo: {pessoa[2]}\nSexo: {pessoa[2]}\nIdade: {pessoa[3]}')     
      else:
          print(f'Pessoa com ID {pessoa_id} não encontrada.')
    except ValueError:
      print("Escolha uma opcao do menu")

def cadastrar():
  while True: 
    pessoas['nome'] = input('Digite o nome: ').upper()#o dicionario na posição nome recebe um input

    while True:
      pessoas['sexo'] = input('Digite o sexo da pessoa M/F:').upper()[0]
      if pessoas['sexo'] in 'F/M':#abreviação para tratar a entrada(se pessoa naposiç~~ao sexo contem as iniciais m ou f )
        break 
      else:
        print('Escolha entre as opcaes M/F: ')
    
    while True:
      try:
        pessoas['idade'] =int(input('Em qual ano nasceu?: '))
        pessoas['idade']=(2024-pessoas['idade'])#calculo da idade do candidato par armazenar apena a idade
        if pessoas['idade']> 0 and pessoas['idade'] <=120:
          break
        else:
          print("verifique o ano de nascimento")
          continue
      except ValueError:
        print('Digite um valor numerico: ')
        continue
    
    inserir_pessoa(cursor,conectar,pessoas)

    while True:   
      stop=input('\nDeseja cadatrar mais um candidato S/N: ').upper()[0]#usando esse metodo separamos a primeira letra ou posição [0]
      if stop in 'S/N':
        break 
    if stop == 'N':
      break


#Inicio do sistema

conectar,cursor=conexao()
#criar_tabela(cursor)

while True:
  menu=input("\nEscolha uma das Opcoes:\n0-Sair\n1-Cadastrar\n2-Listar por Sexo\n3-Media de idade\n4-Listar por ID\n5-Total de pessoas\n>>")
  if menu == "0":
    cursor.close()
    conectar.close()
    break
  elif menu== "1":
    cadastrar()
  elif menu== "2":
    print('\nNomes das mulheres cadastradas:')
    for nome in lista_sexo(cursor, 'F'):
        print(nome[0])
    print('\n\nNomes dos homens cadastrados:')
    for nome in lista_sexo(cursor, 'M'):
        print(nome[0])
  elif menu =="3":
    media_idade = media_idade(cursor)
    print(f'\n\nMédia de idade: {media_idade:.2f}')
  elif menu=="4":
    id_por_pessoa()
  elif menu=="5":
    print(f'\nTotal de pessoas cadastradas: {contar_pessoa(cursor)} pessoas')