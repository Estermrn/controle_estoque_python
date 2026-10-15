from categoria import Categoria, Embalagem, Tamanho, cadastrar_categoria, listar_categorias, buscar_categoria, \
    alterar_categoria, excluir_categoria
from produto import Produto, Unidade, cadastrar_produto, listar_produtos, buscar_produto, excluir_produto


def main():
    print('========================')
    print('  CONTROLE DE ESTOOQUE')
    print('========================')
    print()
    print('Sistema iniciado com sucesso.')
    print()

    categorias = []
    produtos = []

    cadastrar_categoria(categorias)
    listar_categorias(categorias)

    cadastrar_produto(produtos, categorias)
    listar_produtos(produtos)

    procurar_produto = input("Digite o nome do produto que deseja encontrar: ")
    resultado = buscar_produto(produtos, procurar_produto)
    if resultado is not None:
        print("Produto encontrado")
    else:
        print("Produto não encontrado")

    alterar = input("Digite o nome do produto que deseja alterar: ")
    resultado = buscar_produto(produtos, alterar)
    if resultado:
        print("Produto alterado com sucesso")
    else:
        print("Produto não encontrado")

    apagar_prod = input("Digite o nome do produto que deseja apagar: ")
    resultado = excluir_produto(produtos, apagar_prod)
    if resultado:
        print("Produto apagado com sucesso")
    else:
        print("Produto não encontrado")
        
    buscar_nome = input("Digite o nome da categoria que quer procurar: ")
    resultado = buscar_categoria(categorias, buscar_nome)
    if resultado is not None:
        print("Categoria encontrada")
    else:
        print("Categoria não encontrada")

    alterar = input("Digite o nome da categoria que deseja alterar: ")
    resultado = alterar_categoria(categorias, alterar)
    if resultado:
        print("Categoria alterada com sucesso")
    else:
        print("Categoria não encontrada")

    apagar_cat = input("Digite o nome da categoria que deseja excluir: ")
    resultado = excluir_categoria(categorias, apagar_cat)
    if resultado:
        print("Categoria apagada com sucesso")
    else:
        print("Categoria não encontrada")

if __name__ == '__main__':
    main()