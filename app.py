import subprocess

restaurantes = []


def main():
    subprocess.run(["clear"], check=True)
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


def cadastrar_novo_restaurante():
    subprocess.run(["clear"], check=True)
    print("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com suceso.")
    input("\nDigite enter para voltar ao menu principal")
    main()


def listar_restaurantes():
    subprocess.run(["clear"], check=True)
    # fazer def listar restaurante


def ativar_restaurante():
    subprocess.run(["clear"], check=True)
    # fazer def ativar restaurante


def finalizar_app():
    subprocess.run(["clear"], check=True)
    print("App Finalizado\n")


def opcao_invalida():
    print("\nOpção Invalida")
    input("\nDigite qualquer tecla para retornar ao menu: ")
    main()


if __name__ == "__main__":
    main()
