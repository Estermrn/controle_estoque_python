from categoria import Categoria
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




