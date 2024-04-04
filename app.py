from os import name

restaurants = [{'nome': 'Comida', 'categoria': 'Comida', 'ativo': False}, {'nome': 'Pão', 'categoria': 'Comida', 'ativo': True}]

def title(title):
    """Função responsavel por criar titulos padronizados ao centro de 40 espaços com "-" preenchedo as áreas em branco.

    Args:
        title (str): Recebe do main o titulo para padronização
    
    Vars:
        length_word (int):  Recebe um tamanho de 40 espaços menos o tamanho do titulo dividido por dois para inicio e fim caso par,
                            Caso impar soma 1 ao tamanho do titulo para que ele possa se tornar par.

    Outputs:
        {'-'*length_word} (str): Escapa os hifens do inicio do título e do final do titulo.
        {title if len(title)% 2 == 0 else title.append(" ")} (str): Escapa o titulo centralizado entre os hifens iniciais e finais caso par,
                                                                    Caso impar adciona um espaço em branco ao fim do titulo.
            Ex: -----------------Example ----------------- (impar)
                -----------------Examples----------------- (par)
    """
    clear()
    length_word = ( 40 - (len(title) if len(title)% 2 == 0 else len(title)+ 1) ) // 2
    print(f'''
{'-'*length_word}{title if len(title)% 2 == 0 else title.append(" ")}{'-'*length_word}
\n''')

def clear():
    """Função responsavel por identificar qual o sistema está sendo usado e limpar a tela do terminal ou cmd de forma automática.

    Vars:
        system_name (class 'posix.uname_result'): Coleta informações do sistema para identificar qual a versão do OS(Operational System).
    
    """
    import os

    system_name = os.uname()

    if system_name.sysname == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def out_option():
    """Função responsavel por fechar a funcionalidade atual e voltar para o menu.

    inputs:
        input("Digite qualquer tecla para continuar "): Tem apenas a função de confirmar se o usuário viu todas as informações antes de sair.

    Functions:
        clear() : Função localizada em outro trecho do programa, responsavel por limpara a tela.
        main()  : Função localizada em outro trecho do programa, responsavel por voltar para a tela principal. 
    """
    input("\nDigite qualquer tecla para continuar ")
    clear()
    main()

def register_restaurant():
    """Função responsavel por cadastrar um novo dicionario com os dados de um novo restaurante.

    Vars:
        name_rest (str): Variavel que recebe o nome do restaurante.
        category_rest (str): Variavel que recebe uma breve descrição do restaurante sobre o que produz de alimento.
        data_rest (dic): Variavel que recebe um dicionario com:
            'nome' para nome de restaurantes.
            'categoria' para descrição do restaurante.
            'ativo' para status de atividade do restaurante.
    
    Inputs:
        input("Digite o nome do restaurante: ") (str): Recebe entrada com nome do restaurante.
        input(f"Digite a categoria do restaurante {name_rest}: ") (str): Recebe entrada com descrição do restaurante.
    
    Outputs:
        print(f"O restaurante {name_rest} foi cadastrado com sucesso!"): Escapa mensagem de cadastro bem sucedido do "name_rest" para nome do restaurante.

    Functions:
        title(): Função localizada em outro trecho do programa, responsavel por exibir o titulo do programa.
        out_option(): Função localizada em outro trecho do programa, responsavel por sair e voltar para o menu.
    """
    title("Cadastro de restaurantes")

    name_rest = str(input("Digite o nome do restaurante: "))
    category_rest = str(input(f"Digite a categoria do restaurante {name_rest}: "))
    
    data_rest = {'nome': name_rest, 'categoria': category_rest, 'ativo': False}

    restaurants.append(data_rest)
    
    print("\n")
    print(f"O restaurante {name_rest} foi cadastrado com sucesso!")
    out_option()

def list_restaurant(type):
    """Exibe uma listagem com os restaurantes e seus dados separados por uma linha de '-' hifens em 40 espaços.

    Args:
        type (int): Se for igual a 0 sai da listagem assim que termina de listar e volta para o menu,
                    Se for diferente de 0 apenas sai da listagem e mas não volta para o menu, quando listagem usada em outra função.

    Outputs:
        print(f"Nome: {restaurant['nome']} \nCategoria: {restaurant['categoria']} \nAtivação: {'ativado' if restaurant['ativo'] else 'desativado'}"):
            Exibe dados do restaurante separados por linhas:
                linha 1: Nome: nome do restaurante.
                linha 2: Categoria: descrição do restaurante.
                linha 3: Ativação: status de ativado ou desativado.
        print("-"*40): Escapa uma linha de 40 hifens para separar os restaurantes

    Functions:
        title(): Função localizada em outro trecho do programa, responsavel por exibir o titulo do programa.
        out_option(): Função localizada em outro trecho do programa, responsavel por sair e voltar para o menu.   
    
    """
    title("Lista de restaurantes")
    for restaurant in restaurants:
        print(f"Nome: {restaurant['nome']} \nCategoria: {restaurant['categoria']} \nAtivação: {'ativado' if restaurant['ativo'] else 'desativado'}")
        print("-"*40)

    if type == 0:
        out_option()

def status_restaurant():
    """Função responsavel por mudar o status de um restaurante para ativo ou inativo.

    Vars:
        name (str): Recebe o nome do restaurante digitado pelo usuário.
        restaurant_found (bool): Recebe um status de restaurante encontrado ou não pelo laço for.
        msg (str): Recebe mensagem de status alterado para ativo ou inativo do restaurante.
    
    Inputs:
        input("Digite o nome do restaurante que deseja ativar: "): Recebe o nome do restaurante digitado pelo usuário para a busca dentro do dicionario.

    Outputs:
        print(msg): Escapa a mensagem de status ativo ou inativo.
        print(f"O restaurante {name} não foi encontrado."): Escapa mensagem informando que o restaurante não foi encontrado.

    Functions:
        title(): Função localizada em outro trecho do programa, responsavel por exibir o titulo do programa.
        out_option(): Função localizada em outro trecho do programa, responsavel por sair e voltar para o menu
    """
    title("Ativar restaurantes")

    list_restaurant(type=1)
    print("\n")

    name = str(input("Digite o nome do restaurante que deseja ativar: ")).lower().strip()
    print("\n")
    restaurant_found = False
    for restaurant in restaurants:

        if name == str(restaurant['nome']).lower().strip():
            restaurant_found = True
            restaurant['ativo'] = not restaurant['ativo']
            msg = f"O restaurante {name} foi ativado com sucesso" if restaurant['ativo'] else f"O restaurante {name} foi desativado com sucesso."
            print(msg)
        
    if not restaurant_found:
        print(f"O restaurante {name} não foi encontrado.")
            
    out_option()

def exitProg():
    """Função responsavel por fechar o programa.

    Functions:
        title(): Função localizada em outro trecho do programa, responsavel por exibir o titulo do programa.
        clear(): Função localizada em outro trecho do programa, responsavel por limpara a tela do terminal ou do cmd.
    """
    import time

    clear()
    
    title("Saíndo ... ")
    time.sleep(1)
    clear()

def errSytem(opt):
    """Função responsavel por apresenta mensagens de erro de digitação.
    
    Outputs:
        print(f"\"{opt}\" não é uma opção válida, Digite uma opção válida"): Escapa informações sobre uma opção selecionada que não é válida.

    Functions:
        out_option(): Função localizada em outro trecho do programa, responsavel por sair e voltar para o menu.
    """
    print("\n ")
    print(f"\"{opt}\" não é uma opção válida, Digite uma opção válida")
    out_option()

def main():
    """Função main trecho principal do sistema.

    Vars:
        opt (str): Recebe opção digitada pelo usuário do indice da opção do menu para ser convertido para inteiro no futuro.

    Inputs:
        input("Digite a opção que deseja a partir do indice: "): Recebe um valor correspondente a algum indice de opção do menu.
    
    Outputs:
        print(f"{' ':>10}1. Cadastrar restaurante"): Exibe a opção 1 do menu, cadastrar restaurantes.
        print(f"{' ':>10}2. Listar restaurante"): Exibe a opção 2 do menu, listar restaurantes.
        print(f"{' ':>10}3. Alternar status restaurante"): Exibe a opção 3 do menu, ativar restaurantes.
        print(f"{' ':>10}4. Sair\n"): Exibe a opção 4 do menu, sair da aplicação.
    
    Functions:
        register_restaurant(): Função localizada em outro trecho do programa, responsavel por registrar novos restaurantes.
        list_restaurant(): Função localizada em outro trecho do programa, responsavel por listar os restaurantes.
        status_restaurant(): Função localizada em outro trecho do programa, responsavel por alternar status dos restaurantes para ativo ou inativo.
        exitProg(): Função localizada em outro trecho do programa, responsavel por sair da aplicação.
        errSytem(opt): Função localizada em outro trecho do programa, responsavel por exibir mensagem de erro em opções inválidas.

    """
    print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █ █ █▀▀ █▀▄ ██▄ ▄█ ▄█
    
""")

    print(f"{' ':>10}1. Cadastrar restaurante")
    print(f"{' ':>10}2. Listar restaurante")
    print(f"{' ':>10}3. Alternar status restaurante")
    print(f"{' ':>10}4. Sair\n")

    opt = input("Digite a opção que deseja a partir do indice: ")
    try:
        opt = int(opt)
        match opt:
            case 1:
                register_restaurant()
            case 2:
                list_restaurant(type=0)
            case 3:
                status_restaurant()
            case 4:
                exitProg()
            case _:
                errSytem(opt)
    except:
        errSytem(opt)

if __name__ == '__main__':
    main()
