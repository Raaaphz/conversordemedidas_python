continuar = True

while continuar == True:
    print('---CONVERSOR DE MEDIDAS---')
    modo = int(input('1. Comprimento // 2. Volume // 3. Massa // 4. Temperatura  '))
    medida = float(0)
    um1 = int(0)
    um2 = int(0)

    if modo == 1:
        print('Insira a unidade de medida INICIAL')
        print('(1. km // 2. hm // 3. dam // 4. m // 5. dm // 6. cm // 7. mm // 8. Milha // 9. Jarda)  ')
        um1 = int(input())
        medida = float(input('Insira o comprimento: '))
        print('Insira a unidade de medida FINAL')
        print('(1. km // 2. hm // 3. dam // 4. m // 5. dm // 6. cm // 7. mm // 8. Milha // 9. Jarda)  ')
        um2 = int(input())

        if um1 == 1:
            medida = medida * 1000
        elif um1 == 2:
            medida = medida * 100
        elif um1 == 3:
            medida = medida * 10
        elif um1 == 4:
            medida = medida * 1
        elif um1 == 5:
            medida = medida / 10
        elif um1 == 6:
            medida = medida / 100
        elif um1 == 7:
            medida = medida / 1000
        elif um1 == 8:
            medida = medida / 0.0006213
        elif um1 == 9:
            medida = medida / 1.0936
        else:
            print('Número digitado na UNIDADE DE MEDIDA INICIAL invalido')

        if um2 == 1:
            medida = medida / 1000
            validado = True
        elif um2 == 2:
            medida = medida / 100
            validado = True
        elif um2 == 3:
            medida = medida / 10
            validado = True
        elif um2 == 4:
            medida = medida / 1
            validado = True
        elif um2 == 5:
            medida = medida * 10
            validado = True
        elif um2 == 6:
            medida = medida * 100
            validado = True
        elif um2 == 7:
            medida = medida * 1000
            validado = True
        elif um2 == 8:
            medida = medida * 0.00062137
            validado = True
        elif um2 == 9:
            medida = medida * 1.0936
            validado = True

        else:
            print('Número digitado na UNIDADE DE MEDIDA FINAL invalido')
            validado = False
        
        if validado == True:
            print(medida)
        else:
            print('algo deu errado, tente novamente')

        continuarChoice = int(input('Digite 1 para CONTINUAR e 0 para PARAR: '))

        if continuarChoice == 1:
            continuar = True
        else:
            continuar = False

    elif modo == 2:
        print('Insira a unidade de medida INICIAL')
        print('(1. kl(km³) // 2. hl(hm³) // 3. dal(dam³) // 4. l(m³) // 5. dl(dm³) // 6. cl(cm³) // 7. ml(mm³))  ')
        um1 = int(input())
        medida = float(input('Insira o volume: '))
        print('Insira a unidade de medida FINAL')
        print('(1. kl(km³) // 2. hl(hm³) // 3. dal(dam³) // 4. l(m³) // 5. dl(dm³) // 6. cl(cm³) // 7. ml(mm³))  ')
        um2 = int(input())

        if um1 == 1:
            medida = medida * 1000
        elif um1 == 2:
            medida = medida * 100
        elif um1 == 3:
            medida = medida * 10
        elif um1 == 4:
            medida = medida * 1
        elif um1 == 5:
            medida = medida / 10
        elif um1 == 6:
            medida = medida / 100
        elif um1 == 7:
            medida = medida / 1000
        else:
            print('Número digitado na UNIDADE DE MEDIDA INICIAL invalido')
        
        if um2 == 1:
            medida = medida / 1000
            validado = True
        elif um2 == 2:
            medida = medida / 100
            validado = True
        elif um2 == 3:
            medida = medida / 10
            validado = True
        elif um2 == 4:
            medida = medida / 1
            validado = True
        elif um2 == 5:
            medida = medida * 10
            validado = True
        elif um2 == 6:
            medida = medida * 100
            validado = True
        elif um2 == 7:
            medida = medida * 1000
            validado = True
        else:
            print('Número digitado na UNIDADE DE MEDIDA FINAL invalido')
            validado = False
        
        if validado == True:
            print(medida)
        
        continuarChoice = int(input('Digite 1 para CONTINUAR e 0 para PARAR: '))

        if continuarChoice == 1:
            continuar = True
        else:
            continuar = False

    elif modo == 3:
        print('Insira a unidade de medida INICIAL')
        print('(1. kg // 2. hg // 3. dag // 4. g // 5. dg // 6. cg // 7. mg // 8. Tonelada // 9. Libra)  ')
        um1 = int(input())
        medida = float(input('Insira a massa: '))
        print('Insira a unidade de medida FINAL')
        print('(1. kg // 2. hg // 3. dag // 4. g // 5. dg // 6. cg // 7. mg // 8. Tonelada // 9. Libra)  ')
        um2 = int(input())

        if um1 == 1:
            medida = medida * 1000
        elif um1 == 2:
            medida = medida * 100
        elif um1 == 3:
            medida = medida * 10
        elif um1 == 4:
            medida = medida * 1
        elif um1 == 5:
            medida = medida / 10
        elif um1 == 6:
            medida = medida / 100
        elif um1 == 7:
            medida = medida / 1000
        elif um1 == 8:
            medida = medida * 1000000
        elif um1 == 9:
            medida = medida / 0.0022046
        else:
            print('Número digitado na UNIDADE DE MEDIDA INICIAL invalido')
        
        if um2 == 1:
            medida = medida / 1000
            validado = True
        elif um2 == 2:
            medida = medida / 100
            validado = True
        elif um2 == 3:
            medida = medida / 10
            validado = True
        elif um2 == 4:
            medida = medida / 1
            validado = True
        elif um2 == 5:
            medida = medida * 10
            validado = True
        elif um2 == 6:
            medida = medida * 100
            validado = True
        elif um2 == 7:
            medida = medida * 1000
            validado = True
        elif um2 == 8:
            medida = medida / 1000000
            validado = True
        elif um2 == 9:
            medida = medida * 0.0022046
            validado = True
        else:
            print('Número digitado na UNIDADE DE MEDIDA FINAL invalido')
            validado = False
        
        if validado == True:
            print(medida)

        continuarChoice = int(input('Digite 1 para CONTINUAR e 0 para PARAR: '))

        if continuarChoice == 1:
            continuar = True

    elif modo == 4:
        print('Insira a unidade de medida INICIAL')
        print('1. °C // 2 °F // 3. K')
        um1 = int(input())
        medida = float(input('Insira a temperatura: '))
        print('Insira a unidade de medida FINAL')
        print('1. °C // 2 °F // 3. K')
        um2 = int(input())

        if um1 == 1:
            if um2 == 1:
                medida = medida
                validado = True
            elif um2 == 2:
                fatorF =float(0)
                fatorF = 9/5
                medida = medida * fatorF
                medida = medida + 32
                validado = True
            elif um2 == 3:
                medida = medida + 273.15
                validado = True
            else:
                print('Número digitado na UNIDADE DE MEDIDA FINAL invalido')
                validado = False

        elif um1 == 2:
            if um2 == 1:
                medida = medida - 32
                fatorF = float(0)
                fatorF = 5/9
                medida = medida * fatorF
                validado = True
            elif um2 == 2:
                medida = medida
                validado = True
            elif um2 == 3:
                medida = medida - 32
                fatorF = float(0)
                fatorF = 5/9
                medida = medida * fatorF
                medida = medida + 273.15
                validado = True
            else:
                print('Número digitado na UNIDADE DE MEDIDA FINAL invalido')
                validado = False

        elif um1 == 3:
            if um2 == 1:
                medida = medida - 273.15
                validado = True
            elif um2 == 2:
                medida = medida - 273.15
                fatorF =float(0)
                fatorF = 9/5
                medida = medida * fatorF
                medida = medida + 32
                validado = True
            elif um2 == 3:
                medida = medida
                validado = True
            else:
                print('Número digitado na UNIDADE DE MEDIDA FINAL invalido')
                validado = False

        else:
            print('Número digitado na UNIDADE DE MEDIDA INICIAL invalido')
            validado = False

        if validado == True:
            print(medida)

        continuarChoice = int(input('Digite 1 para CONTINUAR e 0 para PARAR: '))

        if continuarChoice == 1:
            continuar = True
        else:
            continuar = False