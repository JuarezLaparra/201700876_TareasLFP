
cadenaestado1 = '--------------------------------------------A1' 
cadenaestados1 = '--AAAAA1' 


def AFD(entradas):
    estado = 0

    for i in range(len(entradas)):
        if estado == 0:
            if entradas[i] == '-':
                estado = 1
            elif entradas[i] == 'A':
                estado = 2
            else:
                print("ERROR CADENA INCORRECTA!!!!")
                return
        elif estado == 1:
            if entradas[i] == '-':
                estado = 1
            elif entradas[i] == 'A':
                estado = 3
            else:
                print("ERROR CADENA INCORRECTA!!!!")
                return
        elif estado == 2:
            if entradas[i] == '1':
                estado = 4
            elif entradas[i] == 'A':
                estado = 2
            else:
                print("ERROR CADENA INCORRECTA!!!!")
                return 
        elif estado == 3:
            if entradas[i] == '1':
                estado = 4
            else:
                print("ERROR CADENA INCORRECTA!!!!")
                return
        elif estado == 4:
            if entradas[i] == '1':
                estado = 4
            elif entradas[i] == '1':
                estado = 4
            else:
                print("ERROR CADENA INCORRECTA!!!!")
                return

    print ("CADENA CORRECTA !!!")

AFD(cadenaestado1)
AFD(cadenaestados1)
