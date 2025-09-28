# Sistema de Classificação de Substâncias com Base no pH
# Solicita ao usuário um valor de pH
ph = float(input("Digite um valor de pH entre 0 e 14: "))

# Verifica se o valor está dentro do intervalo válido
if ph < 0 or ph > 14:
    print("Valor de pH inválido! Deve estar entre 0 e 14.")
elif ph > 7:
    print("Básico")
elif ph < 7:
    print("Ácido")
else:
    print("Neutro")