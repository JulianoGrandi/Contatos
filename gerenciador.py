
def add_cont(name_contact="Sem Nome", num_phone="Sem Numero", email_cont="Sem email", favorite="n"):
  contacts = {"name": name_contact, "phone": num_phone, "email": email_cont, "favorite": False }
  if favorite.lower() == "s":
    contacts["favorite"] = True
  elif favorite.lower() == "n":
    contacts["favorite"] = False 
  lista.append(contacts)
  print(f"contato de {name_contact} adcionado com sucesso")

def view_fav_cont(contacts):
  print("\n Contatos favoritos:")
  for indice, contact in enumerate(lista, start=1):
    if contact["favorite"] == True:
      print(f"{indice}. ★ {contact['name']}, {contact["phone"]}, {contact["email"]}")

def view_cont(contacts):
  print("\n Contatos:")
  contact_ord = sorted(lista, key=lambda c: not c ["favorite"])
  for indice, contact in enumerate(contact_ord, start=1):
    if contact["favorite"] == True:
      print(f"{indice}. ★ {contact['name']}, {contact["phone"]}, {contact["email"]}")
    else:  
      print(f"{indice}.   {contact['name']}, {contact["phone"]}, {contact["email"]}")

def edit_cont(indice, contact=None, phone=None, email=None, favorite= None):
  indice_ajd = indice - 1
  if indice_ajd >= 0 and indice_ajd < len(lista):
    if contact is not None:
      lista[indice_ajd]["name"] = new_name
    if phone is not None:
      lista[indice_ajd]["phone"] = new_phone
    if email is not None:
      lista[indice_ajd]['email'] = new_email
    if favorite is not None:
      lista[indice_ajd][favorite] = new_fav.lower()
  return

def delet_cont(indice):
  indice_ajt = indice - 1
  if indice_ajt >= 0 and indice_ajt < len(lista):
    lista.pop(indice_ajt) 
  else:
    print("Número invalido")


lista = [
    {"name": "Maria", "phone": "1199999-1111", "email": "maria@email.com", "favorite": True},
    {"name": "João", "phone": "1188888-2222", "email": "joao@email.com", "favorite": False},
    {"name": "Ana", "phone": "1177777-3333", "email": "ana@email.com", "favorite": True},
    {"name": "Pedro", "phone": "1166666-4444", "email": "pedro@email.com", "favorite": False},
    {"name": "Lucas", "phone": "1155555-5555", "email": "lucas@email.com", "favorite": True},
    {"name": "Beatriz", "phone": "1144444-6666", "email": "beatriz@email.com", "favorite": False}
    ]

while True:

  print("\nlista de Contatos")
  print("\n1. Adcionar contatos")
  print("2. Ver contatos Favoritos")
  print("3. Ver contatos")
  print("4. Editar contatos")
  print("5. Excluir contatos")
  print("0. Sair ")


  escolha = input("Escolha sua Opção: ")


  if escolha == "0":
    break

  elif escolha == "1":
    name_contact = input("Insira o nome do contato:")
    phone = input("Insira o Número do contato:")
    email = input("Insira o Email do contato:")
    favorite = input("Informe se o contato é favorito s/n:")
    add_cont(name_contact,phone,email,favorite)

  elif escolha == "2":
    view_fav_cont(lista)

  elif escolha == "3":
    view_cont(lista)

  elif escolha == "4":
    view_cont(lista)
    edit_num = int(input("\nQual numero deseja editar?:"))

    print("\n O Que você deseja editar")
    print("1. Nome.")
    print("2. Telefone.")
    print("3. Email.")
    print("4. Se é favorito ou Não.")
    print("5. Tudo.")
    print("0. Sair.")

    edit_quest = input("Qual Opção deseja?:")

    if escolha == "0":
        break
    
    if edit_quest == "1":
      new_name = input("Qual o novo nome do contato?:")
      edit_cont(edit_num,new_name)
      print("Nome alterado com sucesso")

    elif edit_quest == "2":
      new_phone = input("Qual é o novo número?:")
      edit_cont(edit_num,None,new_phone)
      print("Número alterado com sucesso")

    elif edit_quest == "3":
      new_email = input("Qual é o novo email?:")
      edit_cont(edit_num,None,None,new_email)
      print("Email alterado com sucesso")

    elif edit_quest == "4":
      new_fav = input("É favorito s/n?")
      edit_cont(edit_num,None,None,None,new_fav)
      print("Favorito alterado com sucesso")

    elif edit_quest == "5":
      new_name = input("Qual o novo nome do contato?:")
      new_phone = input("Qual é o novo número?:")
      new_email = input("Qual é o novo email?:")
      new_fav = input("É favorito s/n?")
      edit_cont(edit_num,new_name,new_phone,new_email,new_fav)
      print("Dados alterados com sucesso")

  elif escolha == "5":
    view_cont(lista)
    dele_cont = int(input("Qual contato deseja deletar?:"))
    delet_cont(dele_cont)
    print("Contato deletado com sucesso.")
    

 