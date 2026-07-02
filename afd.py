estado = "q0"
palavra = input("Digite uma sequência de 0 e 1: ")

for simbolo in palavra:
    estado_anterior = estado
    
    if estado == "q0":
        if simbolo == "1":
            estado = "q1"
    elif estado == "q1":
        if simbolo == "1":
            estado = "q0"
            
    print(f"{estado_anterior} --{simbolo}--> {estado}")

if estado == "q0":
    print("Palavra aceita!")
else:
    print("Palavra rejeitada!")