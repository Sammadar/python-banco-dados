# CRUD em camadas com Python e MySQL

Aplicação de terminal para cadastro de clientes e produtos, feita para praticar a separação em
camadas: conexão com o banco, repositórios que executam o SQL e telas que conversam com o usuário.
O menu usa a biblioteca `questionary`, então dá para navegar com as setas.

Projeto de curso.

## Como rodar

1. Crie o banco rodando `src/database/estrutura.sql` no MySQL. No Windows o `my_sql.bat` faz isso;
   ajuste usuário e senha no início do arquivo.
2. Instale as dependências. O `script.bat` cria o ambiente virtual e instala tudo; ou manualmente:

```bash
pip install -r requirements.txt
python main.py
```

## Estrutura

```
main.py                 menu principal (Clientes, Produtos, Sair)
src/database/           estrutura.sql cria o banco; conexao.py abre a conexão
src/Repositorios/       insert, update, delete e select de clientes e produtos
src/telas/              telas de cada cadastro, que chamam os repositórios
```

Cada camada só conhece a de baixo: a tela não escreve SQL e o repositório não imprime nada.

Python · MySQL · mysql-connector · questionary · rich
