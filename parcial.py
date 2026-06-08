#datos
codigos =[]
nombres=[]
precios =[]
stocks=[]
#menu principal
opcion=0
while opcion !=7:
    print("="*30)
    print("--- SUPERMERCADO PYTHON MARKET ---")
    print("1. Cargar producto")
    print("2. Mostrar producto")
    print("3. Buscar producto")
    print("4. Ordenar productos por precio")
    print("5. Mostrar producto con menor stock")
    print("6. Calcular valor total del inventario")
    print("7. Salir")
    opcion=int(input("Selecciona una opcion: "))
    if opcion == 1:
        codigo_nuevo = int(input("Codigo: "))
        repetido=False
        for i in range(len(codigos)):
            if codigos[i] == codigo_nuevo:
             repetido = True
        if repetido:
            print("ERROR: codigo existente")
        else:
            nombre_nuevo= input("Nombre del producto: ")
            #validar precio mayor a cero
            precio_nuevo=float(input("Precio: "))
            while precio_nuevo <=0:
                print("ERROR: el precio debe ser mayor a cero")
                precio_nuevo= float(input("Precio: "))

                #No puede ser negativo
            stock_nuevo = int(input("Stock: "))
            while stock_nuevo < 0:
                print("ERROR:el stock no puede ser negativo")
                stock_nuevo = int(input("Stock: "))
            #guardar en la lista     
            codigos.append(codigo_nuevo)
            nombres.append(nombre_nuevo)
            precios.append(precio_nuevo)
            stocks.append(stock_nuevo)
    elif opcion == 2:
        if len(codigos)==0:
            print("Sin productos")
        else:
            print("codigo|nombre|precio|stock")
            for i in range (len(codigos)):
                print(f"{codigos[i]}|{nombres[i]}|{precios[i]}|{stocks[i]}")
    elif opcion == 3:
        if len(codigos) == 0:
            print("Esta vacio")
        else:
            buscar=int (input("codigo a buscar: "))
            encontro=False
            for i in range(len(codigos)):
                if codigos[i]==buscar:
                    print(f"producto encontrado: ") 
                    print(f"nombre:{nombres[i]}") 
                    print(f"precio:{precios[i]}")   
                    print(f"stock:{stocks[i]}")  
                    encontro=True
                    break
                if not encontro:
                    print("Codigo no existente") 
    elif opcion == 4:
        if len(precios)<2:
            print("No hay productos suficientes para ordenar")
        else:
            for i in range(len(precios)-1):
                for j in range (len(precios)-1 -i):
                    if precios[j]>precios[j+1]:
                        #orden de precios
                        aux=precios[j]
                        precios[j]=precios[j+1]
                        precios[j+1]=aux
                        #orden de codigos
                        aux=codigos[j]
                        codigos[j]=codigos[j+1]
                        codigos[j+1]=aux
                        #orden nombres
                        aux =nombres[j]
                        nombres[j]=nombres[j+1]
                        nombres[j+1]=aux
                        #orden stocks
                        aux=stocks[i]
                        stocks[j]=stocks[j+1]
                        stocks[j+1]=aux
                    print("Precio Orden de menor a mayor")
                    for i in range(len(precios)):
                        print(f"{codigos[i]} - {nombres[i]} - {precios[i]} - {stocks[i]}")
    elif opcion == 5:
        if len(stocks)==0:
            print ("Stock vacio")
        else:
            menor =stocks[0]
            sto=0
            for i in range(1,len(stocks)):
                if stocks[i]<menor:
                    menor = stocks[i]
                    sto=i
            print("producto con menor cantidad de stock: ")
            print(f"nombre: {nombres[sto]}")
            print(f"stock: {stocks[sto]}")
    elif opcion == 6:
        if len(precios)==0:
            print("valor total $0.00")
        else:
            total=0
            for i in range(len(precios)):
                total +=(precios[i]*stocks[i])
            print(f"El Valor total es: ${total:.2f} ")
