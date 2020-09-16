#! /usr/bin/python3
#Había un encabezado que no correspondía, e impedía ejecutar. 
ingreso=int(input("ELIJA UNA OCPION: INGRESAR CLIENTE= 1 \n SALIR=0"))
while ingreso==1:
    #Generalmente se acostumbra usar minúsculas para las variables
    # (es solo cuestión de estilo, anda igual).
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
        print("DESCUENTO DE:", -DESC)
        print("TOTAL: $",PRECIOTOTAL)
        ELEGIR=int(input("ELIJA UNA OPCION: HONDA=1 \n YAMAHA=2 \n SUZUKI=3 \n SALIR=0"))
    print("ERROR ELIJA OTRA OPCION:")
    if ELEGIR ==0:
        ingreso=int(input("ELIJA UNA OPCION: INGRESAR CLIENTE= 1 \n SALIR =0"))

