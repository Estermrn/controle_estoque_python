from categoria import Categoria, buscar_categoria
from enum import Enum

class Unidade(Enum):
    QUILOS = "Quilogramas"
    LITROS = "Litros"
    GRAMAS = "Gramas"
    MILILITROS = "Mililitros"

class Produto:
    #O atributo unidade passa a representar o Enum Unidade
    def __init__(
        self,
        nome: str,
        preco_unitario: float,
        unidade: Unidade,
        quantidade_estoque: int,
        quantidade_minima: int,
        quantidade_maxima: int,
        categoria: Categoria
        ):

        self.nome = nome
        self.preco_unitario = preco_unitario
        self.unidade = unidade
        self.quantidade_estoque = quantidade_estoque
        self.quantidade_minima = quantidade_minima
        self.quantidade_maxima = quantidade_maxima
        self.categoria = categoria

    def adicionar_estoque(self, quantidade: int):
        if quantidade <= 0:
            print("Não é possível adicionar uma quantidade menor do que zero")
        elif self.quantidade_estoque + quantidade > self.quantidade_maxima:
            print("Não é possível adicionar uma quantidade maior do que a máxima permitida")
        else:
            self.quantidade_estoque += quantidade

    def remover_estoque(self, quantidade: int):
        if  quantidade <= 0:
            print("Não é possível remover uma quantidade menor ou igual a zero")
        elif quantidade > self.quantidade_estoque:
            print("Não é possível remover uma quantidade maior do que a em estoque")
        else:
            self.quantidade_estoque -= quantidade

    def estoque_baixo(self):
        return self.quantidade_estoque < self.quantidade_minima

def cadastrar_produto(produtos, categorias):
    nome = input("Digite o nome do produto: ")

    try:
        preco = float(input("Digite o preço do produto: R$"))
    except ValueError:
        print("Preço inválido")
        return

    unidade = input("Digite o tipo de unidade: ")
    try:
        unidade = Unidade(unidade)
    except ValueError:
        print("Tamanho inválido")
        return

    try:
        quantidade = int(input("Digite a quantidade: "))
        quantidade_min = int(input("Digite a quantidade mínima: "))
        quantidade_max = int(input("Digite a quantidade máxima: "))
    except ValueError:
        print("As quantidades devems ser números inteiros")
        return

    categoria = input("Digite a categoria desejada: ")
    resultado = buscar_categoria(categorias, categoria)
    if resultado is not None:
        produto = Produto(
            nome,
            preco,
            unidade,
            quantidade,
            quantidade_min,
            quantidade_max,
            resultado
        )

        produtos.append(produto)

def listar_produtos(lista):
    for numero, produto in enumerate(lista, start=1):
        print(numero, "-", produto.nome)

def buscar_produto(lista, nome_buscado):
    for produto in lista:
        if produto.nome == nome_buscado:
            return produto

    return None

def alterar_produto(lista, nome, categorias):
    produto = buscar_produto(lista, nome)

    if produto is not None:
        novo_nome = input("Digite o novo nome do produto: ")
        produto.nome = novo_nome
        novo_preco = input("Digite o novo preço: ")
        produto.preco_unitario = novo_preco
        nova_unidade = input("Digite a nova unidade: ")
        produto.unidade = nova_unidade
        novo_estoque = input("Digite a nova quantidade em estoque: ")
        produto.quantidade_estoque = novo_estoque
        novo_minimo = input("Digite a nova quantidade mínima em estoque: ")
        produto.quantidade_minima = novo_minimo
        novo_maximo = input("Digite a nova quantidade máxima em estoque: ")
        produto.quantidade_maxima = novo_maximo

        categoria_nova = input("Digite a nova categoria: ")
        resultado = buscar_categoria(categorias, categoria_nova)
        if resultado is not None:
            produto.categoria = resultado
        return True

    return False

def excluir_produto(lista, nome):
    produto = buscar_produto(lista, nome)

    if produto is not None:
        lista.remove(produto)
        return True

    return False
