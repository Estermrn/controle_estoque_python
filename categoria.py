class Categoria: #Criação de uma classe Categoria
    def __init__(self, nome, tamanho, embalagem): #Vai ser iniciado quando um objeto categoria for criado
       #Irá receber os valores dos objetos criados e colocar dentro de cada atributo correspondente
        self.nome = nome
        self.tamanho = tamanho
        self.embalagem = embalagem
