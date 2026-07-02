transicoes = {("q0", "a"): {"q0", "q1"}, ("q1", "b"): {"q2"}}
estado_inicial = {"q0"}
estado_final = {"q2"}

palavra = input("Digite uma palavra: ")
estados = estado_inicial

for simbolo in palavra:
    novos = set()
    for estado in estados:
        if (estado, simbolo) in transicoes:
            novos.update(transicoes[(estado, simbolo)])
    estados = novos

if estados & estado_final:
    print("Palavra aceita!")
else:
    print("Palavra rejeitada!")