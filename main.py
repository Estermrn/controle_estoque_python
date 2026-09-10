from categoria import Categoria, Tamanho, Embalagem


def main():
    print('========================')
    print('  CONTROLE DE ESTOOQUE')
    print('========================')
    print()
    print('Sistema iniciado com sucesso.')

    #Criação do objeto categoria, definindo o nome, tamanho e embalagem
    categoria = Categoria(
        "Bebidas",
        Tamanho.MEDIO,
        Embalagem.PLASTICO 
    )

if __name__ == '__main__':
    main()