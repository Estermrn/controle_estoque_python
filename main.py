from categoria import Categoria

def main():
    print('========================')
    print('  CONTROLE DE ESTOOQUE')
    print('========================')
    print()
    print('Sistema iniciado com sucesso.')

    #Criação do objeto categoria, definindo o nome, tamanho e embalagem
    categoria = Categoria(
        "Bebidas",
        "Médio",
        "Plástico"
    )

if __name__ == '__main__':
    main()