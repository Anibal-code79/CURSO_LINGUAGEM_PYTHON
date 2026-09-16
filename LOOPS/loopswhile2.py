numero=int(input(
    """
     ================================================
    | Ola seja benvindo ao nosso Jogo de adivinhar   |
    | o nmero secreto do magico. Digite um  numero   |
    | para adivinhar o numero secreto do magico:     |
     ================================================
    """))
numero_secreto=5

while numero!=numero_secreto: 
    print("Ha ha! Você está preso no meu loop!")
    numero=int(input("Digite um  numero para adivinhar o numero secreto do magico e sair do loop: "))

print("Muito bem, trouxa! Você está livre agora.")