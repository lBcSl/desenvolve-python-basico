import csv
import os

# Função para limpar a tela do console
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir menu principal
def exibir_menu_principal():
    limpar_tela()
    print("=== Bem-vindo ao Sistema de Gerenciamento da Empresa ===")
    print("Escolha uma opção:")
    print("1. Gerenciamento de Usuários")
    print("2. Gerenciamento de Produtos/Serviços")
    print("3. Sair do Sistema")
    opcao = input("Digite o número da opção desejada: ")
    return opcao

# Função para salvar usuários em arquivo CSV
def salvar_usuarios(usuarios):
    with open('usuarios.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
        campos = ['nome', 'senha', 'permissao']
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        for usuario in usuarios:
            escritor_csv.writerow(usuario)

# Função para carregar usuários do arquivo CSV
def carregar_usuarios():
    usuarios = []
    try:
        with open('usuarios.csv', mode='r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            for linha in leitor_csv:
                usuarios.append(linha)
    except FileNotFoundError:
        # Se o arquivo não existir ainda, retorna uma lista vazia
        pass
    return usuarios

# Função para cadastrar novo usuário
def cadastrar_usuario():
    print("=== Cadastro de Novo Usuário ===")
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")
    permissao = input("Digite o nível de permissão (1 - Admin, 2 - Usuário Comum): ")
    return {'nome': nome, 'senha': senha, 'permissao': permissao}

# Função para listar todos os usuários
def listar_usuarios(usuarios):
    limpar_tela()
    print("=== Listagem de Usuários ===")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']} | Permissão: {usuario['permissao']}")

# Função para buscar usuário por nome
def buscar_usuario_por_nome(usuarios, nome):
    for usuario in usuarios:
        if usuario['nome'] == nome:
            return usuario
    return None

# Função para editar informações de um usuário
def editar_usuario(usuarios):
    print("=== Edição de Usuário ===")
    nome = input("Digite o nome do usuário que deseja editar: ")
    usuario = buscar_usuario_por_nome(usuarios, nome)
    if usuario:
        print(f"Usuário encontrado: {usuario['nome']} | Permissão: {usuario['permissao']}")
        nova_permissao = input("Digite a nova permissão (1 - Admin, 2 - Usuário Comum): ")
        usuario['permissao'] = nova_permissao
        salvar_usuarios(usuarios)
        print("Usuário atualizado com sucesso!")
    else:
        print("Usuário não encontrado!")

# Função para excluir um usuário
def excluir_usuario(usuarios):
    print("=== Exclusão de Usuário ===")
    nome = input("Digite o nome do usuário que deseja excluir: ")
    usuario = buscar_usuario_por_nome(usuarios, nome)
    if usuario:
        usuarios.remove(usuario)
        salvar_usuarios(usuarios)
        print("Usuário excluído com sucesso!")
    else:
        print("Usuário não encontrado!")

# Função para gerenciar usuários
def gerenciar_usuarios():
    usuarios = carregar_usuarios()
    while True:
        print("\n")
        print("=== Gerenciamento de Usuários ===")
        print("Escolha uma opção:")
        print("1. Cadastrar Novo Usuário")
        print("2. Listar Todos os Usuários")
        print("3. Editar Usuário")
        print("4. Excluir Usuário")
        print("5. Voltar ao Menu Principal")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            novo_usuario = cadastrar_usuario()
            usuarios.append(novo_usuario)
            salvar_usuarios(usuarios)
            print("Usuário cadastrado com sucesso!")

        elif opcao == '2':
            listar_usuarios(usuarios)

        elif opcao == '3':
            editar_usuario(usuarios)

        elif opcao == '4':
            excluir_usuario(usuarios)

        elif opcao == '5':
            salvar_usuarios(usuarios)
            break

        else:
            print("Opção inválida. Digite novamente.")

# Função para salvar produtos em arquivo CSV
def salvar_produtos(produtos):
    with open('produtos.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
        campos = ['nome', 'preco', 'quantidade']
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        for produto in produtos:
            escritor_csv.writerow(produto)

# Função para carregar produtos do arquivo CSV
def carregar_produtos():
    produtos = []
    try:
        with open('produtos.csv', mode='r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            for linha in leitor_csv:
                produtos.append(linha)
    except FileNotFoundError:
        # Se o arquivo não existir ainda, retorna uma lista vazia
        pass
    return produtos

# Função para cadastrar novo produto
def cadastrar_produto():
    print("=== Cadastro de Novo Produto ===")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    return {'nome': nome, 'preco': preco, 'quantidade': quantidade}

# Função para listar todos os produtos
def listar_produtos(produtos):
    limpar_tela()
    print("=== Listagem de Produtos ===")
    for produto in produtos:
        print(f"Nome: {produto['nome']} | Preço: R${produto['preco']} | Quantidade: {produto['quantidade']}")

# Função para buscar produto por nome
def buscar_produto_por_nome(produtos, nome):
    for produto in produtos:
        if produto['nome'] == nome:
            return produto
    return None

# Função para ordenar produtos por nome
def ordenar_produtos_por_nome(produtos):
    return sorted(produtos, key=lambda x: x['nome'])

# Função para ordenar produtos por preço
def ordenar_produtos_por_preco(produtos):
    return sorted(produtos, key=lambda x: x['preco'])

# Função para editar informações de um produto
def editar_produto(produtos):
    print("=== Edição de Produto ===")
    nome = input("Digite o nome do produto que deseja editar: ")
    produto = buscar_produto_por_nome(produtos, nome)
    if produto:
        print(f"Produto encontrado: {produto['nome']} | Preço: R${produto['preco']} | Quantidade: {produto['quantidade']}")
        novo_preco = float(input("Digite o novo preço do produto: "))
        nova_quantidade = int(input("Digite a nova quantidade em estoque: "))
        produto['preco'] = novo_preco
        produto['quantidade'] = nova_quantidade
        salvar_produtos(produtos)
        print("Produto atualizado com sucesso!")
    else:
        print("Produto não encontrado!")

# Função para excluir um produto
def excluir_produto(produtos):
    print("=== Exclusão de Produto ===")
    nome = input("Digite o nome do produto que deseja excluir: ")
    produto = buscar_produto_por_nome(produtos, nome)
    if produto:
        produtos.remove(produto)
        salvar_produtos(produtos)
        print("Produto excluído com sucesso!")
    else:
        print("Produto não encontrado!")

# Função para gerenciar produtos
def gerenciar_produtos():
    produtos = carregar_produtos()
    while True:
        print("\n")
        print("=== Gerenciamento de Produtos ===")
        print("Escolha uma opção:")
        print("1. Cadastrar Novo Produto")
        print("2. Listar Todos os Produtos")
        print("3. Editar Produto")
        print("4. Excluir Produto")
        print("5. Imprimir Produtos Ordenados por Nome")
        print("6. Imprimir Produtos Ordenados por Preço")
        print("7. Voltar ao Menu Principal")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            novo_produto = cadastrar_produto()
            produtos.append(novo_produto)
            salvar_produtos(produtos)
            print("Produto cadastrado com sucesso!")

        elif opcao == '2':
            listar_produtos(produtos)

       
