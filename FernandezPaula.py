Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>
Ingreso= (int(input("ELIJA UNA OCPION: INGRESAR CLIENTE= 1 \n, SALIR=0))
while Ingreso ==1:
    ELEGIR=int(input("ELIJA UNA OPCION: HONDA=1 \n YAMAHA=2 \n SUZUKI = 3 \n SALIR = 0"))
    while ELEGIR >=1 and ELEGIR<=4:
        PRECIO= int(input("INGRESE EL PRECIO:"))
        print("TOTAL: $",PRECIO)
        ELEGIR=int(input("ELIJA UNA OPCION: HONDA=1 \n YAMAHA=2 \n SUZUKI=3 \n SALIR=0"))

