# Documentação de Software: Cadastro Simplificado de Pessoas com MySQL.

## Descrição Geral
Este projeto visa a criação de um sistema simples de cadastro de pessoas utilizando o banco de dados MySQL para armazenar informações. O sistema é implementado em Python, utilizando a biblioteca `mysql.connector` para conectar e manipular o banco de dados. Ele oferece funcionalidades para cadastrar, listar e consultar pessoas no banco de dados, além de calcular a média de idade e listar pessoas por sexo.

## Tecnologias Utilizadas
- ![Python Icon](https://img.icons8.com/color/48/000000/python--v1.png) **Python**: Linguagem de programação para implementação das regras de negócio e integração com o banco de dados.
- ![MySQL Icon](https://img.icons8.com/fluency/48/000000/mysql-logo.png) **MySQL**: Sistema de gerenciamento de banco de dados relacional utilizado para armazenar as informações das pessoas cadastradas.
- ![MySQL Connector Icon](https://img.icons8.com/fluency/48/000000/database.png) **MySQL Connector**: Biblioteca Python para conectar e executar operações em um banco de dados MySQL.

## Funcionalidades Principais
- **Cadastro de Pessoas**: O sistema coleta nome, sexo e idade e os armazena no banco de dados.
- **Listagem por Sexo**: Exibe as pessoas cadastradas, separadas por sexo.
- **Média de Idade**: Calcula e exibe a média de idade das pessoas cadastradas.
- **Consulta por ID**: Permite consultar os detalhes de uma pessoa específica, informando o ID.
- **Contagem Total de Pessoas**: Exibe o total de pessoas cadastradas no banco de dados.

## Estrutura do Código
### Conexão com o Banco de Dados
- **Função `conexao`**: Estabelece uma conexão com o banco de dados MySQL e retorna o cursor para manipular os dados.

### Criação da Tabela
- **Função `criar_tabela`**: Cria a tabela "pessoas" caso ela ainda não exista no banco de dados.

### Inserção de Dados
- **Função `inserir_pessoa`**: Insere os dados de uma pessoa no banco de dados.

### Consulta e Relatórios
- **Função `contar_pessoa`**: Retorna o número total de pessoas cadastradas.
- **Função `lista_sexo`**: Lista as pessoas cadastradas por sexo.
- **Função `media_idade`**: Calcula a média de idade das pessoas.
- **Função `id_pessoa`**: Consulta e retorna as informações de uma pessoa pelo ID.
- **Função `id_por_pessoa`**: Interage com o usuário para buscar uma pessoa específica pelo ID.

### Cadastro de Pessoas
- **Função `cadastrar`**: Coleta os dados da pessoa (nome, sexo, idade) e faz a inserção no banco de dados.

## Fluxo de Execução
O sistema inicia estabelecendo a conexão com o banco de dados e, a partir daí, exibe um menu com as seguintes opções:

1. **Cadastrar**: Coleta e insere os dados de uma nova pessoa.
2. **Listar por Sexo**: Exibe as pessoas cadastradas por sexo.
3. **Média de Idade**: Calcula e exibe a média de idade das pessoas cadastradas.
4. **Consultar por ID**: Exibe os dados de uma pessoa específica informando o ID.
5. **Total de Pessoas**: Exibe o total de pessoas cadastradas no banco de dados.

### Exemplo de Uso

```
    Escolha uma das Opções:
    0-Sair
    1-Cadastrar
    2-Listar por Sexo
    3-Média de idade
    4-Listar por ID
    5-Total de pessoas

```
