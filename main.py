from categoria import Categoria, Embalagem, Tamanho, cadastrar_categoria, listar_categorias, buscar_categoria, \
    alterar_categoria, excluir_categoria
from produto import Produto, Unidade, cadastrar_produto, listar_produtos, buscar_produto, excluir_produto, \
    reajustar_preco, alterar_produto


def main():
    print('========================')
    print('  CONTROLE DE ESTOOQUE')
    print('========================')
    print()
    print('Sistema iniciado com sucesso.')
    print()

    categorias = []
    produtos = []


    while True:
        print("========== MENU PRINCIPAL ==========")
        print("1 - Gerenciar categorias")
        print("2 - Gerenciar produtos")
        print("3 - Reajustar preços")
        print("0 - Sair")
        print()
        opcao = int(input("Esolha uma opção: "))
        print()
        match opcao:

            case 1:
                while True:
                    print("===== GERENCIAR CATEGORIAS =====")
                    print("1 - Cadastrar categorias")
                    print("2 - Listar categorias")
                    print("3 - Buscar categorias")
                    print("4 - Alterar categorias")
                    print("5 - Apagar categorias")
                    print("0 - Sair")
                    print()
                    opcao_cat = int(input("Escolha uma opção: "))
                    print()
                    match opcao_cat:
                        case 1:
                            print("↓↓↓ Cadastrar categorias ↓↓↓")
                            cadastrar_categoria(categorias)
                            print()
                        case 2:
                            print("↓↓↓ Listar categorias ↓↓↓")
                            listar_categorias(categorias)
                            print()
                        case 3:
                            print("↓↓↓ Buscar categorias ↓↓↓")
                            buscar_cat = input("Digite o nome da categoria que quer procurar: ")
                            resultado = buscar_categoria(categorias, buscar_cat)
                            if resultado is not None:
                                print("Categoria encontrada")
                            else:
                                print("Categoria não encontrada")
                        case 4:
                            print("↓↓↓ Alterar categorias ↓↓↓")
                            alterar_cat = input("Digite o nome da categoria que deseja alterar: ")
                            resultado = alterar_categoria(categorias, alterar_cat)
                            if resultado:
                                print("Categoria alterada com sucesso")
                            else:
                                print("Categoria não encontrada")
                        case 5:
                            print("↓↓↓ Apagar categorias ↓↓↓")
                            apagar_cat = input("Digite o nome da categoria que deseja excluir: ")
                            resultado = excluir_categoria(categorias, apagar_cat)
                            if resultado:
                                print("Categoria apagada com sucesso")
                            else:
                                print("Categoria não encontrada")
                        case 0:
                            break
                        case _:
                            print("Opção inválida")
            case 2:
                while True:
                    print("===== GERENCIAR PRODUTOS =====")
                    print("1 - Cadastrar produtos")
                    print("2 - Listar produtos")
                    print("3 - Buscar produtos")
                    print("4 - Alterar produtos")
                    print("5 - Excluir produtos")
                    print("0 - Sair")
                    print()
                    opcao_prod = int(input("Escolha uma opção: "))
                    print()
                    match opcao_prod:
                        case 1:
                            print("↓↓↓ Cadastrar produto ↓↓↓")
                            cadastrar_produto(produtos, categorias)
                            print()
                        case 2:
                            print("↓↓↓ Listar produtos ↓↓↓")
                            listar_produtos(produtos)
                            print()
                        case 3:
                            print("↓↓↓ Buscar produtos ↓↓↓")
                            procurar_produto = input("Digite o nome do produto que deseja encontrar: ")
                            resultado = buscar_produto(produtos, procurar_produto)
                            if resultado is not None:
                                print("Produto encontrado")
                            else:
                                print("Produto não encontrado")
                        case 4:
                            print("↓↓↓ Alterar produtos ↓↓↓")
                            alterar_prod = input("Digite o nome do produto que deseja alterar: ")
                            resultado = alterar_produto(produtos, alterar_prod, categorias)
                            if resultado:
                                print("Produto alterado com sucesso")
                            else:
                                print("Produto não encontrado")
                        case 5:
                            print("↓↓↓ Excluir produtos ↓↓↓")
                            apagar_prod = input("Digite o nome do produto que deseja apagar: ")
                            resultado = excluir_produto(produtos, apagar_prod)
                            if resultado:
                                print("Produto apagado com sucesso")
                            else:
                                print("Produto não encontrado")
                        case 0:
                            break
                        case _:
                            print("Opção inválida")
            case 3:
                print("↓↓↓ Reajustar preços ↓↓↓")
                try:
                    reajuste = float(input("Digite o percentual de ajuste: "))
                    resultado = reajustar_preco(produtos, reajuste)
                    if resultado:
                        print("Sucesso! Preço reajustado em {}%".format(reajuste))
                        listar_produtos(produtos)
                    else:
                        print("Erro! Os produtos não podem ser reajustados")
                except ValueError:
                    print("Percentual inválido!")
            case 0:
                break
            case _:
                print("Opção inválida")

if __name__ == '__main__':
    main()