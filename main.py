cpf = "77777777777"

num1 = float(cpf[0:1])
num2 = float(cpf[1:2])
num3 = float(cpf[2:3])
num4 = float(cpf[3:4])
num5 = float(cpf[4:5])
num6 = float(cpf[5:6])
num7 = float(cpf[6:7])
num8 = float(cpf[7:8])
num9 = float(cpf[8:9])
num10 = float(cpf[9:10])
num11 = float(cpf[10:11])

def valida1(cpf):

    if num1 != num2 or num2 != num3 or num3 != num4 or num4 != num5 or num5 != num6 or num6 != num7 or num7 != num8 or num8 != num9 or num9 != num10 or num10 != num11:
        return
    return False


def validado_1_digito(cpf):
    soma1 = (num1 * 10 + num2 * 9 + num3 * 8 + num4 * 7 +
     num5 * 6 + num6 * 5 + num7 * 4 + num8 * 3 + num9 * 2)
    print(soma1)

    resto1 = (soma1 * 10) % 11
    print(resto1)
    if resto1 == 10:
        return resto1 == 0
    else:
        return resto1


def validacao_2_digito():
    soma2 = (num1 * 11 + num2 * 10 + num3 * 9
    + num4 * 8 + num5 * 7 + num6 * 6 + num7 * 5
    + num8 * 4 + num9 * 3 + num10 * 2)
    print(soma2)
    resto2 = (soma2 * 10) % 11
    print(resto2)

    if resto2 == 10:
        return resto2 == 0
    else:
        return resto2

def validacao2 (num10, num11, resto1, resto2):
    print(validacao2(num10, num11, resto1, resto2))
    if (resto1 == num10) and (resto2 == num11):
        return True
    else:
        return False




valida1(cpf)
validado_1_digito(cpf)
validacao_2_digito()

print(valida1(cpf))
print(validado_1_digito(cpf))
print(validacao_2_digito())
