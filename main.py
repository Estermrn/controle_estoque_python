from categoria import Categoria, Embalagem, Tamanho, cadastrar_categoria, listar_categorias, buscar_categoria, \
    alterar_categoria, excluir_categoria
from produto import Produto, Unidade

def main():
    print('========================')
    print('  CONTROLE DE ESTOOQUE')
    print('========================')
    print()
    print('Sistema iniciado com sucesso.')
    print()

    categorias = []

    cadastrar_categoria(categorias)
    listar_categorias(categorias)

    buscar_nome = input("Digite o nome da categoria que quer procurar: ")
    resultado = buscar_categoria(categorias, buscar_nome)
    if resultado is not None:
        print("Categoria encontrada")
    else:
        print("Categoria não encontrada")

    print()

    alterar = input("Digite o nome da categoria que deseja alterar: ")
    resultado = alterar_categoria(categorias, alterar)
    if resultado:
        print("Categoria alterada com sucesso")
    else:
        print("Categoria não encontrada")

    apagar = input("Digite o nome da categoria que deseja excluir: ")
    resultado = excluir_categoria(categorias, apagar)
    if resultado:
        print("Categoria apagada com sucesso")
    else:
        print("Categoria não encontrada")

if __name__ == '__main__':
    main()