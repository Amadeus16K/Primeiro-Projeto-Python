# Inicio do Código fonte:

def adicionar_tarefas(descricao):  # Declarando a função para adicionar tarefas
    try:  # Instrução para lidar com o Except
        # Abrindo o arquivo de dados para adicionar informação
        with open("arquivo.txt", "a") as arquivo:
            # Indicando a função que vai ser atribuida ao adicionar tarefas
            arquivo.write(descricao + "\n")
            # Mostrar na tela a mensagem caso dê certo
            print("Tarefa adicionada com sucesso!")
    except Exception as e:  # Excação caso aconteça algum erro
        print("Erro ao adicionar tarefa: ", e)  # Mensagem de erro


def visualizar_tarefas():       # Declarando a função de Visualizar Tarefas
    try:        # Instrução para lidar com o Except
        # Abrindo o arquivo de dados para adicionar informação
        with open("arquivo.txt", "r") as arquivo:
            # Indicando a função que vai ser atribuida ao visualizar tarefas
            tarefas = arquivo.readlines()
            if not tarefas:     # Se não tiver tarefas
                print("Não há atividades!")     # Mostrar na tela
            else:  # Se tiver tarefas
                print("Lista com tarefas: ")        # Mostrar na tela
                # Enumerar cada atividade começando do número 1
                for i, tarefas in enumerate(tarefas, start=1):
                    # Mostrar na tela o némero e a respectiva atividade
                    print(f"{i}. {tarefas.strip()}")
    except FileNotFoundError:  # Caso dê algum erro no arquivo
        print("Arquivo de tarefas não encontrado!")  # Mostrar isso
    except Exception as e:      # Ou se for problema no código
        print("Erro ao visualizar tarefas...", e)       # Mostrar isso


# Declarando a função de Marcar a tarefa como concluída
def marcar_tarefa_concluida(numero):
    try:        # Instrução para lidar com o Except
        # Abrindo o arquivo para poder adicionar ou tirar informação
        with open("arquivo.txt", "r") as arquivo:
            tarefas = arquivo.readlines()       # Lendo as linhas do arquivo
        if len(tarefas) >= numero:  # Visualizador da lista
            # Atribuindo a diminuição da tarefa que foi concluída
            tarefa_concluida = tarefas.pop(numero - 1)
            with open("arquivo.txt", "w") as arquivo:  # Abrindo novamente o arquivo de dados
                arquivo.writelines(tarefas)  # Escrevendo/Manipulando os dados
            # Mostrando na tela a mensagem de sucesso
            print(f"Tarefa '{tarefa_concluida.strip()
                             }' marcada como concluída")
        else:  # Se não...
            # Mostrando na tela a mensagem de erro
            print("Número de tarefa errado!")
    except FileNotFoundError:       # Uma exceção, caso o arquivo não seja encontrado
        # Mostrando na tela a mensagem, indicando que não encontrou o arquivo
        print("Arquivo de tarefas não encontrado!")
    except Exception as e:      # Outra exceção
        # Mostrando que deu erro ao visualizar a tarefa
        print("Erro ao visualizar tarefas...", e)


def excluir_tarefa(numero):         # Declarando a função para apagar a tarefa
    try:    # Instrução para lidar com o Except
        with open("arquivo.txt", "r") as arquivo:  # Abrindo o arquivo para poder tirar informação
            tarefas = arquivo.readlines()       # Lendo as linhas do arquivo
        if len(tarefas) >= numero:  # Mostrando a lista
            # Atribuindo a diminuição da tarefa
            tarefa_excluida = tarefas.pop(numero - 1)
            with open("arquivo.txt", "w") as arquivo:       # Abrindo novamente o arquivo
                # Fazendo mudança no arquivo
                arquivo.writelines(tarefas)
            # Mensagem exibida na tela caso êxito
            print(f"Tarefa foi '{tarefa_excluida.strip()}' excluída.")
        else:           # Se não...
            # Mostrando na tela a mensagem de erro caso o némero não exista
            print("Número de tarefa inválido.")
    except FileNotFoundError:       # Excecção caso o arquivo não seja encontrado
        # Mensagem impressa na tela caso não seja encontrado
        print("Arquivo de tarefas não encontrado.")
    except Exception as e:          # Outra exceção
        # Mostrando na tela que não foi possivel excluir a tarefa
        print("Erro ao excluir tarefa:", e)

# Aqui mostra o inicio do código de de funcionamento e o que vai ser impresso na tela:


def menu():         # Definindo uma função
    # Imprimindo na tela a primeira informação
    print("\nSelecione uma opção:")
    print("1. Adicionar tarefa")            # Imprimindo na tela as opções
    print("2. Visualizar tarefa")           # Imprimindo na tela as opções
    print("3. Marcar tarefa como concluída")  # Imprimindo na tela as opções
    print("4. Excluir tarefa")              # Imprimindo na tela as opções
    print("5. Sair")                        # Imprimindo na tela as opções


def main():         # Definindo outra função
    while True:     # Indicando loop infinito
        menu()      # Escolha
        # Entrada de dados
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':        # Caso o numero escolhido seja o 1, acontece...
            # Entrada de dados
            descricao = input("Digite a descrição da tarefa: ")
            # Adicionando dados no arquivo
            adicionar_tarefas(descricao)

        elif opcao == '2':      # Caso o numero escolhido seja o 1, acontece...
            visualizar_tarefas()  # Visualizar as tarefas

        elif opcao == '3':  # Caso o numero escolhido seja o 3, acontece...
            # Entrada de dados no arquivo
            numero = int(input("Digite o número da tarefa a ser concluída: "))
            # Marca a tarefa como concluída
            marcar_tarefa_concluida(numero)

        elif opcao == '4':      # Caso o numero escolhido seja o 1, acontece...
            # Entrada de dados
            numero = int(input("Digite o número da tarefa a ser excluída: "))
            excluir_tarefa(numero)      # Exclui a tarefa excolhida

        elif opcao == '5':      # Caso o numero escolhido seja o 5, acontece...
            # Entrada de dados
            print("Saindo do programa... Bye")
            break       # Quebra o loop

        else:           # Caso não aconteça nada acima
            # Mostra essa mensagem
            print("Opção invalida. Tente novamente...")


if __name__ == "__main__":  # Verifica se o scrpt está sendo executado corretamente
    main()
