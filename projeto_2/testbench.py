from pyfunctions.functions import *
registry_list = []

i = 0
while i <= 100 or i == 0:
  user = userSelection()
  
  if user.mode == 1:
    registry_list.append(shapePoint())
    i = i + 1
    input('\nForma registrada! Pressione Enter para voltar: ')
  
  elif user.mode == 2:
    registry_list.append(shapeLine())
    i = i + 1
    input('\nForma registrada! Pressione Enter para voltar: ')
  
  elif user.mode == 3:
    registry_list.append(shapeSquare())
    i = i + 1
    input('\nForma registrada! Pressione Enter para voltar: ')
    
  elif user.mode == 4:
    registry_list.append(shapeRectangle())
    i = i + 1
    input('\nForma registrada! Pressione Enter para voltar: ')
    
  elif user.mode == 5:
    registry_list.append(shapeCircle())
    i = i + 1
    input('\nForma registrada! Pressione Enter para voltar: ')
    
  elif user.mode == 9:
    if i == 0:
      input('Nenhuma forma geométrica registrada. Pressione Enter para voltar: ')
      
    if i > 0:
      print('\nFormas geométricas registradas:')
      for x in range(0, i):
        print(f'{x}. {registry_list[x].shapeType}')
        
      userRegistry = input('\nInsira o número da forma geométrica a ser verificada: ')
      userRegistry = int(userRegistry)
      
      if userRegistry <= i-1:
        print(f'- Forma geométrica: {registry_list[userRegistry].shapeType}')
        print(registry_list[userRegistry].string)
        input('Pressione Enter para voltar: ')
      else:
        input('ERRO: Número selecionado é inválido. Pressione Enter para voltar: ')
        
  elif user.mode == 0:
    break
  
  else:
    input('Escolha inválida. Pressione Enter para voltar: ')
