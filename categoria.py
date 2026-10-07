from enum import Enum

#Criação da classe para definir o tamanho
class Tamanho(Enum): #Representa os tamanhos permitidos
    #Cada membro possuí um valor associado a ele
    PEQUENO = "Pequeno"
    MEDIO = "Médio"
    GRANDE = "Grande"

#Criação da classe para definir a embalagem
class Embalagem(Enum): #Representa as embalagens permitidas
    #Cada membro terá um valor associado para ser apresentado depois
    LATA = "Lata"
    VIDRO = "Vidro"
    PLASTICO = "Plástico"
    ORGANICO = "Orgânico"

class Categoria: #Criação de uma classe Categoria
    def __init__(
        self,
        nome: str,
        tamanho: Tamanho,
        embalagem: Embalagem
        ):#Vai ser iniciado quando um objeto categoria for criado

        #Irá receber os valores dos objetos criados e colocar dentro de cada atributo correspondente
        self.nome = nome
        self.tamanho = tamanho
        self.embalagem = embalagem

def cadastrar_categoria(categorias):
    print("Iniciando cadastro de categoria")

    nome = input("Digite o nome da categoria: ")
    tamanho = input("Digite o tamanho: ")
    try:
        tamanho = Tamanho(tamanho)
    except ValueError:
        print("Tamanho inválido")
        return

    embalagem = input("Digite a embalagem: ")
    try:
        embalagem = Embalagem(embalagem)
    except ValueError:
        print("Embalagem inválida")
        return

    categoria = Categoria(
        nome,
        tamanho,
        embalagem
    )

    categorias.append(categoria)

def listar_categorias(lista):
    for numero, categoria in enumerate(lista, start=1):
        print(numero, "-", categoria.nome)

def buscar_categoria(lista, nome_buscado):
    for categoria in lista:
        if categoria.nome == nome_buscado:
            return categoria

    return None

def alterar_categoria(lista, buscar):
    categoria = buscar_categoria(lista, buscar)

    if categoria is not None:
        novo = input("Digite o novo nome da categoria: ")
        categoria.nome = novo
        return True

    return False

def excluir_categoria(lista, nome):
    categoria = buscar_categoria(lista, nome)

    if categoria is not None:
        lista.remove(categoria)
        return True

    return False
