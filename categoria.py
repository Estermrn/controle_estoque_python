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
