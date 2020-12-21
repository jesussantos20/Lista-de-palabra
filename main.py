numero = int(input("Dígame cúantas palabras tiene la lista:"))
if numero< 1:
  print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
      print("Dígame la palabra", str(i+1)+":",end="")
      palabra = input()
      lista+= [palabra]
      print("la lista creada es:",lista)
      eliminar = input("palabra a eliminar:")
      for i in range(len(lista)-1,-1,-1):
        if lista [i] == eliminar:del(lista[i])
        print("la lista es ahora:",lista)
