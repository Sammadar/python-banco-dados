import questionary
from src.Repositorios import produto_repositorio


def executar_produto():
    opcoes = ["Listar todos", "Cadastrar", "Editar", "Apagar", "Voltar"]
    opcao_desejada = ""
    while opcao_desejada != "Voltar":
        opcao_desejada = questionary.select("Escolha o menu desejado dos produtos", opcoes).ask()
        if opcao_desejada == "Cadastrar":
            __cadatrar()
        elif opcao_desejada == "Listar todos":
            __listar_todos()

def __listar_todos():
    produtos = produto_repositorio.listar_todos()
    print("Lista de produtos: ")
    for produto in produtos:
        print("id:", produto ["id"], "Nome:", produto["nome"])

# Funções com um/dois underline(s) antes do nome são consideradas
# funções privadas, ou seja, n devem/podem ser utilizadas em outros 
# arquivos

def __cadatrar():
# Função responsável por cadastrar um produto, solicitando os dados
#  necessários para o cadastro    
    nome_produto = input ("Digite o nome do produto: ")

# Chamar a função de cadastrar(insert) o produto no banco de dados
#  passando como parâmetro o nome do produto    
    produto_repositorio.cadastrar(nome_produto)

print("Produto cadastrado com sucesso")