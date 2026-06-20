nombre = ""
tipo = ""
nivel = 0
poder = ""

pokedex = ()

def crear_pokemon():
    nombre, tipo, nivel, poder
    
    print("--- REGISTRAR POKEMON ---")
    
    while True:
        nombre = input("ingresar el nombre del pokemon").strip() #elimina los espacios en blanco al principio y al final de un texto (codigo sacado del curso en cisco)
    
        if not nombre:
            print("Error: el nombre no puede estar vacio.")
            continue
        
        duplicado = False
        for p in pokedex:
            if p["nombre"].lower() == nombre.lower():
                duplicado = True
                break
        
        if duplicado:
            print("Errror: este pokemon ya esta registrado en la pokedex.")
            continue
        break

    while True:
        tipo = input("ingresar el tipo (fuego, agua): ").strip() #elimina los espacios en blanco al principio y al final de un texto (codigo sacado del curso en cisco)
    
        if not tipo:
            print("Error:el tipo no puede estar vacio.")
            continue
        break

    while True:
        try:
            nivel = int(input("ingresa el nivel (debe ser un numero entero): "))
            if nivel <= 0:
                print("Error: el nivel tiene que ser mayor a 0.")
                continue
            break


        except ValueError:
            print("Error humano encontrado: es obligatorio un numero entero.")

    while True:
        poder = input("ingresar el poder principal: ").strip() #elimina los espacios en blanco al principio y al final de un texto (codigo sacado del curso en cisco)
    
        if not poder:
            print("Error: el poder no puede estar vacio.")
            continue
        break

    nuevo_pokemon = {
        "Nombre": nombre,
        "Tipo": tipo,
        "Nivel": nivel,
        "Poder": poder
    }
    
    pokedex.append(nuevo_pokemon)
    print(f"{nombre} se registro con exito")

def leer_pokedex():
    print("--- MI POKEDEX ---")
    
    if not pokedex:
        print("la pokedex esta vacia, no hay registros por mostrar.")
        return
        
    for p in pokedex:
        print(f"nombre: {["nombre"]} tipo: {["tipo"]} nivel: {["nivel"]} poder: {["poder"]}")

def actualizar_pokemon():
    print("--- ACTUALIZAR POKEMON ---")
    if not pokedex:
        print("No hay Pokemones registrados por modificar.")
        return

    nombre_buscar = input("ingrese el nombre del pokemon que desee modificar").strip() #elimina los espacios en blanco al principio y al final de un texto (codigo sacado del curso en cisco)
    
    encontrado = None #es la ausencia de un valor (codigo sacado del curso en cisco)
    
    for p in pokedex:
        if p["nombre"].lower() == nombre_buscar.lower():
            encontrado = p
            break
            
    if encontrado is None:  #es la ausencia de un valor (codigo sacado del curso en cisco)
    
        print("Pokemon no encontrado.")
        return

    print(f"modificando a {encontrado['nombre']} introduce los nuevos datos")
    
    while True:
        nuevo_tipo = input("nuevo tipo: ").strip()
        if not nuevo_tipo:
            print("Error: el tipo no puede estar vacio")
            continue
        break

    while True:
        try:
            nuevo_nivel = int(input("un  nuevo nivel (numero entero) "))
            if nuevo_nivel <= 0:
                print("Error: el nivel debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("Error: debes ingresar un numero entero valido")

    while True:
        nuevo_poder = input("nuevo poder").strip()
        if not nuevo_poder:
            print("Error: el poder no puede estar vacio")
            continue
        break

    encontrado["Tipo"] = nuevo_tipo
    encontrado["Nivel"] = nuevo_nivel
    encontrado["Poder"] = nuevo_poder
    print("Pokemon se actualizo con exito")

def eliminar_pokemon():
    print("--- ELIMINAR POKEMON ---")
    if not pokedex:
        print("no se registraron pokemones para eliminar")
        return

    nombre_buscar = input("ingresa el nombre del Pokemon que deseas eliminar ").strip() #elimina los espacios en blanco al principio y al final de un texto (codigo sacado del curso en cisco)
    
    
    encontrado = None #es la ausencia de un valor (codigo sacado del curso en cisco)
    
    for p in pokedex:
        if p["nombre"].lower() == nombre_buscar.lower():
            encontrado = p
            break
            
    if encontrado is None: #es la ausencia de un valor (codigo sacado del curso en cisco)
    
        print("pokemon no encontrado.")
        return

    pokedex.remove(encontrado)
    print(f"{nombre_buscar} ha sido eliminado con exito")

while True:
    print("=================================")
    print(" MENU POKEDEX CRUD ")
    print("=================================")
    print("1. Registrar Pokemon (create) ")
    print("2. Mostrar Pokedex (read) ")
    print("3. Actualizar Pokemon (update) ")
    print("4. Eliminar Pokemon (delete)")
    print("5. Salir")
    print("=================================")
    
    opcion = input("Selecciona una opcion (1-5)").strip() #elimina los espacios en blanco al principio y al final de un texto (codigo sacado del curso en cisco)
    
    
    if opcion == "1":
        crear_pokemon()
    elif opcion == "2":
        leer_pokedex()
    elif opcion == "3":
        actualizar_pokemon()
    elif opcion == "4":
        eliminar_pokemon()
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion no valida. Por favor, ingresa un numero del 1 al 5.")

