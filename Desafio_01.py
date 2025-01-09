def salvar_contato(nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    print("Contato adicionado com sucesso!")
    return contato

def ver_contatos(contatos):
    if not contatos:
        print("Nenhum contato encontrado!")
    else:
        print("\nLista de contatos")
        for indice, contato in enumerate(contatos, start=1):
            favorito = " (Favorito)" if contato["favorito"] else ""
            print(f"ID:{indice} Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}{favorito}")

def editar_contato(contatos):
    print("Você selecionou editar um contato\nQual contato deseja editar?")
    ver_contatos(contatos)
    id_contato = int(input("Digite o ID do contato que deseja editar: "))
    
    if 1 <= id_contato <= len(contatos):
        contato = contatos[id_contato - 1]
        print(f"Contato selecionado: {contato['nome']}, {contato['telefone']}, {contato['email']}")
        novo_nome = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        novo_email = input("Digite o novo email do contato: ")
        contato['nome'] = novo_nome
        contato['telefone'] = novo_telefone
        contato['email'] = novo_email
        print("Contato atualizado com sucesso!")
    else:
        print("ID inválido. Tente novamente.")

def marcar_favorito(contatos):
    print("Você selecionou marcar um contato como favorito\nQual contato deseja marcar?")
    ver_contatos(contatos)
    id_contato = int(input("Digite o ID do contato que deseja marcar como favorito: "))
    
    if 1 <= id_contato <= len(contatos):
        contato = contatos[id_contato - 1]
        contato['favorito'] = True
        print(f"O contato {contato['nome']} foi marcado como favorito!")
    else:
        print("ID inválido. Tente novamente.")
    

def excluir_contato(contatos):
    print("Você selecionou excluir um contato\nQual contato deseja excluir?")
    ver_contatos(contatos)
    id_contato = int(input("Digite o ID do contato que deseja excluir: "))
    if 1 <= id_contato <= len(contatos):
        contato = contatos.pop(id_contato - 1)
        print(f"O contato {contato['nome']} foi excluído com sucesso!")
    else:
        print("ID inválido. Tente novamente.")


contatos = []

while True:
    print("\nSelecione uma opção:")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar contato como favorito")
    print("5. Excluir contato")
    print("6. Sair")
    
    opcao_selecionada = input("Selecione uma opção: ")
    
    if opcao_selecionada == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        contato = salvar_contato(nome, telefone, email)
        contatos.append(contato)
            
    elif opcao_selecionada == "2":
        ver_contatos(contatos)
    
    elif opcao_selecionada == "3":
        editar_contato(contatos)
    
    elif opcao_selecionada == "4":
        marcar_favorito(contatos)
    
    elif opcao_selecionada == "5":
        excluir_contato(contatos)
                
    elif opcao_selecionada == "6":
        print("Você está saindo da lista de contatos!")
        break
    
    else:
        print("Opção inválida! Tente novamente.")