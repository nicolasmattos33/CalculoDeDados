def validar_vetores(v1, v2):
    if len(v1) != len(v2):
        raise ArithmeticError ("Os vetores devem ter o mesmo tamanho !")
    return True

def euclidiana(v1, v2):
    validar_vetores(v1, v2)
    soma_quadrados = sum((a - b) ** 2 for a, b in zip(v1, v2))
    return soma_quadrados ** 0.5

def produto_escalar(v1, v2):
    validar_vetores(v1, v2)
    return sum(a * b for a, b in zip(v1, v2))