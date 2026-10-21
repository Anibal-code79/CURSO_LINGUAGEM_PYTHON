def verificarTriangulo(lado1, lado2, lado3):
    if lado1+lado2>lado3 or lado1+lado3>lado2 or lado2+lado3>lado1:
        return True
    else:
        return False

