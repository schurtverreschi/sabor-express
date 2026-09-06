import subprocess

restaurantes = [
    {"Nome": "Abaré", "Categoria": "Pizzaria", "Status": False},
    {"Nome": "Panela Mineira", "Categoria": "Comida Mineira", "Status": False},
    {"Nome": "Olk", "Categoria": "Hamburgueria", "Status": False},
]


def main():
    exibir_subtitulo("")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")


def exibir_opcoes():
    print("""
1. Cadastrar restaurante
2. Listar Restaurantes
3. Ativar restaurante
4. Sair\n
""")

    # print("1. Cadastrar restaurante")
    # print("2. Listar restaurantes")
    # print("3. Ativar restaurante")
    # print("4. Sair\n")


def escolher_opcao():

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        match opcao_escolhida:
            case 1:
                return cadastrar_novo_restaurante()
            case 2:
                return listar_restaurantes()
            case 3:
                return ativar_restaurante()
            case 4:
                return finalizar_app()
            case _:
                return opcao_invalida()
    except ValueError:
        opcao_invalida()

    # try:
    #     opcao_escolhida = int(input("Escolha uma opção: "))

    #     if opcao_escolhida == 1:
    #         cadastrar_novo_restaurante()
    #     elif opcao_escolhida == 2:
    #         listar_restaurantes()
    #     elif opcao_escolhida == 3:
    #         ativar_restaurante()
    #     elif opcao_escolhida == 4:
    #         finalizar_app()
    #     else:
    #         opcao_invalida()
    # except ValueError:
    #     opcao_invalida()


def exibir_subtitulo(subtitulo):
    subprocess.run(["clear"], check=True)
    print(subtitulo + "\n")


def voltar_menu_principal():
    input("\nDigite enter para voltar ao menu principal")
    main()


def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novo restaurante")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria_do_restaurante = input(
        f"\nDigite a categoria do restaurante {nome_do_restaurante}: "
    )
    restaurante = {
        "Nome": nome_do_restaurante,
        "Categoria": categoria_do_restaurante,
        "Status": False,
    }
    restaurantes.append(restaurante)
    print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso.")
    voltar_menu_principal()


def listar_restaurantes():
    exibir_subtitulo("Lista de restaurantes cadastrados:")
    for restaurante in restaurantes:
        print(
            f"- {restaurante['Nome']} | {restaurante['Categoria']} | {restaurante['Status']}"
        )
    voltar_menu_principal()


def ativar_restaurante():
    exibir_subtitulo("Ativar restaurante")
    # fazer def ativar restaurante
    voltar_menu_principal()


def finalizar_app():
    exibir_subtitulo("App Finalizado")


def opcao_invalida():
    print("\nOpção Invalida")
    voltar_menu_principal()


if __name__ == "__main__":
    main()
