import questionary
from src.Repositorios import cliente_repositorio

def executar_cliente():
    opcoes = ["Listar todos", "Cadastrar", "Editar", "Apagar", "Voltar"]   
    opcao_desejada = ""
    while opcao_desejada != "Voltar":
        opcao_desejada = questionary.select(
            "Por favor, cadastre o nome e o CPF desejado:", opcoes
        ).ask()
        if opcao_desejada == "Cadastrar":
            __cadastrar()
        elif opcao_desejada == "Listar todos":
            __listar_todos()
        elif opcao_desejada == "Editar": 
            __editar() 
        elif opcao_desejada == "Apagar":
            __apagar()

def __cadastrar():
    nome_cliente = questionary.text("Digite o nome: ").ask()
    cpf_clientes = questionary.text("Digite o cpf: ").ask()
    cliente_repositorio.cadastrar(nome_cliente, cpf_clientes)
    print("Cliente cadastrado com sucesso")


def __editar():
    id_para_editar = int(questionary.text("Digite o id do clientes para editar: ").ask())
    novo_nome = questionary.text("Digite o nome: ").ask()
    novo_cpf = questionary.text("Digite o cpf: ").ask()
    cliente_repositorio.editar(id_para_editar, novo_nome, novo_cpf)
    print("Cliente alterado com sucesso")

def __apagar():
    id_para_apagar = int(questionary.text("Digite o id do cliente para apagar: ").ask())
    cliente_repositorio.apagar(id_para_apagar)
    print("Cliente apagado com sucesso")

def __listar_todos():
    clientes = cliente_repositorio.listar_todos()
    print("Lista de Clientes:")
    for clientes in clientes:
        print("Id:", clientes["id"], "Nome:", clientes["nome"], "Cpf:", clientes["cpf"])