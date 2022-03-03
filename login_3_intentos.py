print ("solo cuentas con 3 oportunidades")
contador =1
while contador <=3:
    usuario = input("ingresa usuario: ")
    contraseña = input("Escribe password: ")
    if usuario == "Fernando" and contraseña == "ULA2021":
        print ("Bienvenido al sistema")
        contador =4
    else:
        print(f"Dato incorrectos")
        if contador == 3:
            print ("Favor de ponerse en contacto con el administrador del sistema")
        contador = contador+1