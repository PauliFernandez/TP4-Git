Python 3.7.7 (tags/v3.7.7:d7c567
        08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>
ingreso=int(input("ELIJA UNA OCPION: INGRESAR CLIENTE= 1 \n SALIR=0"))
while ingreso==1:
    ELEGIR=int(input("ELIJA UNA OPCION: HONDA=1 \n YAMAHA=2 \n SUZUKI=3 \n SALIR=0"))
    while ELEGIR >=1 and ELEGIR<=4:
        PRECIO= int(input("INGRESE EL PRECIO:"))
        if ELEGIR==1:
            DESC=(PRECIO*5)/100
        if ELEGIR ==2:
            DESC=(PRECIO*8)/100
        if ELEGIR==3:
            DESC=(PRECIO*10)/100
        if ELEGIR ==4:
            DESC=(PRECIO*2)/100
        PRECIOTOTAL=PRECIO-DESC
        print("DESCUENTO DE:$ ", -DESC)
        print ("TOTAL:$ ", PRECIOTOTAL)
        PAGO = int (input("ELIJA EL MEDIO DE PAGO\n 1.EFECTIVO\n 2.TARJETA"))
        if PAGO == 1:
            PAGOFINAL = PRECIOTOTAL
            print ("PAGO EN EFECTIVO\n RECARGO = 0%\n", "TOTAL:", PAGOFINAL)
        else: 
            RECARGA = ((PRECIOTOTAL*20)/100)
            PAGOFINAL = RECARGA + PRECIOTOTAL
            print ("PAGO EN TARJETA\n", "RECARGO:$ ", RECARGA, "\nTOTAL:", PRECIOTOTAL, "+", RECARGA, "=", PAGOFINAL)
        ELEGIR = int(input("ELIJA UNA OPCION:\n HONDA=1\n YAMAHA=2\n SUZUKI=3\n SALIR=0"))
    ingreso = int(input("ELIJA UNA OPCION:\n INGRESAR CLIENTE=1\n SALIR=0"))

