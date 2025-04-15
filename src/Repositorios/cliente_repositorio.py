from src.database.conexao import abrir_conexao

def cadastrar(nome_cliente: str,  cpf_clientes: str):
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("insert into clientes (nome,cpf) values(%s,%s)", (nome_cliente, cpf_clientes))
        conexao.commit()
        conexao.close()
    except Exception as e:
        print(e)
       
def listar_todos():
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("select id, nome, cpf from clientes")
        registros = cursor.fetchall()
        clientes = []
        
       
        for registro in registros:
            cliente = {
                "id": registro[0],
                "nome": registro[1],
                "cpf": registro[2]
            }
            clientes.append(cliente)
       
        return clientes
    except Exception as err:
       
        print("Não foi possível carregar os Clientes")
        print(err)


def apagar(id_apagar: int):
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id_apagar,))
        conexao.commit()
        conexao.close()
    except Exception as er:
        print("Não foi possível apagar o registro")
        print(er)


def editar(id_editar: int, novo_nome: str, novo_cpf: str):
    try:
        conexao = abrir_conexao()
        cursor = conexao.cursor()
        cursor.execute("UPDATE clientes SET nome = %s, cpf =%s WHERE id = %s", (novo_nome, novo_cpf, id_editar))
        conexao.commit()
        conexao.close()
    except Exception as error:
        print("Não foi possível alterar o cliente")
        print(error)




