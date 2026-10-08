lista_produtos = []


def adicionar_produtos():
    qtd = int(input("Digite a quantidade de produtos: "))

    for numero in range(1, qtd + 1):
        print(f"\n--- Produto {numero} ---")

        nome_produto = input("Digite o nome: ")
        valor = float(input("Digite o preço: R$ ").replace(",", "."))
        tipo = input("Digite a categoria: ")

        novo_produto = {
            "nome": nome_produto,
            "preco": valor,
            "categoria": tipo
        }

        lista_produtos.append(novo_produto)

    print("\nCadastro realizado com sucesso!")


def pesquisar_por_preco():
    if len(lista_produtos) == 0:
        print("\nNão existem produtos cadastrados.")
        return

    valor_referencia = float(
        input("Digite o preço de referência: R$ ").replace(",", ".")
    )

    print("\n[1] Produtos com preço maior")
    print("[2] Produtos com preço menor")

    escolha = input("Digite sua opção: ")

    encontrados = False

    for item in lista_produtos:
        if escolha == "1" and item["preco"] > valor_referencia:
            print(f'{item["nome"]} - R$ {item["preco"]:.2f}')
            encontrados = True

        elif escolha == "2" and item["preco"] < valor_referencia:
            print(f'{item["nome"]} - R$ {item["preco"]:.2f}')
            encontrados = True

    if not encontrados:
        print("Nenhum produto encontrado.")


def mostrar_ordenacao():
    if not lista_produtos:
        print("\nNenhum produto cadastrado.")
        return

    menor_para_maior = sorted(
        lista_produtos,
        key=lambda produto: produto["preco"]
    )

    maior_para_menor = sorted(
        lista_produtos,
        key=lambda produto: produto["preco"],
        reverse=True
    )

    print("\n--- PREÇOS DO MENOR PARA O MAIOR ---")

    for item in menor_para_maior:
        print(f'{item["nome"]} -> R$ {item["preco"]:.2f}')

    print("\n--- PREÇOS DO MAIOR PARA O MENOR ---")

    for item in maior_para_menor:
        print(f'{item["nome"]} -> R$ {item["preco"]:.2f}')


def listar_categorias():
    if not lista_produtos:
        print("\nNenhum produto cadastrado.")
        return

    categorias = set(
        produto["categoria"] for produto in lista_produtos
    )

    print("\n--- CATEGORIAS CADASTRADAS ---")

    for categoria in sorted(categorias):
        print(f"- {categoria}")


def obter_estatisticas():
    if not lista_produtos:
        return None

    valores = []

    for produto in lista_produtos:
        valores.append(produto["preco"])

    menor_valor = min(valores)
    maior_valor = max(valores)
    preco_medio = sum(valores) / len(valores)

    return menor_valor, maior_valor, preco_medio


def exibir_relatorio():
    dados = obter_estatisticas()

    if dados is None:
        print("\nNão há produtos para gerar o relatório.")
        return

    menor, maior, media = dados

    categorias = set()

    for produto in lista_produtos:
        categorias.add(produto["categoria"])

    print("\n" + "=" * 42)
    print("           RELATÓRIO DE PRODUTOS")
    print("=" * 42)

    print(f"Quantidade de produtos: {len(lista_produtos)}")
    print(f"Menor preço: R$ {menor:.2f}")
    print(f"Maior preço: R$ {maior:.2f}")
    print(f"Preço médio: R$ {media:.2f}")
    print(f"Quantidade de categorias: {len(categorias)}")

    print("\n--- LISTA DE PRODUTOS ---")

    for produto in lista_produtos:
        print(
            f'Produto: {produto["nome"]} | '
            f'Preço: R$ {produto["preco"]:.2f} | '
            f'Categoria: {produto["categoria"]}'
        )


def iniciar_programa():
    while True:
        print("\n========== SISTEMA DE PRODUTOS ==========")
        print("1 - Adicionar produtos")
        print("2 - Pesquisar por preço")
        print("3 - Exibir produtos ordenados")
        print("4 - Listar categorias")
        print("5 - Consultar estatísticas")
        print("6 - Gerar relatório")
        print("0 - Encerrar")

        comando = input("Selecione uma opção: ")

        if comando == "1":
            adicionar_produtos()

        elif comando == "2":
            pesquisar_por_preco()

        elif comando == "3":
            mostrar_ordenacao()

        elif comando == "4":
            listar_categorias()

        elif comando == "5":
            dados = obter_estatisticas()

            if dados:
                print("\n--- ESTATÍSTICAS ---")
                print(f"Menor preço: R$ {dados[0]:.2f}")
                print(f"Maior preço: R$ {dados[1]:.2f}")
                print(f"Preço médio: R$ {dados[2]:.2f}")
            else:
                print("\nNenhum produto cadastrado.")

        elif comando == "6":
            exibir_relatorio()

        elif comando == "0":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    iniciar_programa()