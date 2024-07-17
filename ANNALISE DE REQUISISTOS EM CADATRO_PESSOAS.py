pessoas=dict()#criado o dicionario que deve receber as variaveis
lista=list()#criado a ista que vai receber os dicionarios
soma=media=0 #ebreviaçã das funções soma e media em um so linha
type(pessoas)
while True: #laco pricipal que deve repetir todo o processo
  pessoas['nome'] = input('Digite o nome: ').upper()#o dicionario na posição nome recebe um input

  while True:# laco para receber e tratar a variavel nome
    pessoas['sexo'] = input('Digite o sexo da pessoa M/F:').upper()[0]
    if pessoas['sexo'] in 'F/M':#abreviação para tratar a entrada(se pessoa naposiç~~ao sexo contem as iniciais m ou f )
      break #recebe m ou f e para
    else:
      print('Escolha entre as opções M/F: ') # se nao esta entre m ou f volta ao laco
  while True:
    try:# ´precisa tratar tambem os erros para valor nao numericos
      pessoas['idade'] =int(input('Em qual ano nasceu?: '))#entrad acom o ano de nacimento
      pessoas['idade']=(2023-pessoas['idade'])#calculo da idade do candidato par armazenar apena a idade
      soma+=pessoas['idade']#adição de soma com o numerador especial que ler o dicionario pessoas na posição idade e pega o valos inteiro
      break
    except ValueError:
      print('Digite um valor numerico: ')
      continue#retornao ao inicio do laço e pergunta a idade

  lista.append(pessoas.copy())#incorpora a o dikcionario a nova lista de pessoas

  while True:    # novo laço par tratar a resposta sim ou não
    stop=input('\nDeseja cadatrar mais um candidato S/N: ').upper()[0]#usando essemetgodo sepoaramos a primeira letra ou posição [0]
    if stop in 'S/N':
      break #par ao laço de repetição local
      print('Responda "S" ou "N":')
  if stop == 'N':
    break#para o laço de repetição principal e passa para o proximo comando
print('-'*30)
print('\nLista de pessoa(s) cadastrada(s)')
for p in lista:
  for k,v in p.items():
    print(f'{k}={v}' ,end=" ")
print()


print('Cadastramos {} pessoas'.format(len(lista)))#faz aleitura de tgoda o lista e traz o tamanho com todas as variaveis
#print(f'cadastramos{len(lista)} pessoas')
media= soma/len(lista)#media recebe a soma dividida pela le de pessoas no posição nome, uma matematica basica
print('\nA media de idade é {:5.2f}'.format(media))#media fornatada com 5 numero e duas casas decimais ":5.2f"
#print(f'A media de idade é {(media)}')3observe que ha uma maneira de trazer os valores da veriave usando o .format e sua abrevialçao

print('\nA(s) mulher(es) cadastrada(s): ',end =" ")#o ',end=""nao deia quebra a linha
for p in lista: # necessario ler toda a lista e sepaar o sexo
  if p['sexo']== 'F': #ler toda alista de 'p' na posição 'sexo', se que tem "F" como primeira letra
    print(f'{p["nome"]}',end='  ') #foi feito a impressão direta de "p" na posição nome 'p' e o dicionario que contem a pessoa que recebe o nome
print()
print('\nAs pessoas que estão acima da media de idade são:')
for p in lista:#ler  lista e tras as idades acima da media
  if p['idade'] >= media:
    for key, value in p.items():#as chave e os valores do item
      print(f'{key} = {value};' ,end=" ") #print com format de chave e valores dos dicionarios