print("Bienvenidos al calculador de costos de taxis")

tarifa_base = 500
distancia_km = 200
duracion_min = 150
contador = 0
total_km = 0
total_min = 0
total_final = 0

while True:
    contador = contador + 1
    


    distancia_cliente = int(input("ingrese la distancia del viaje en kilometros: "))
    duracion_cliente = int(input("ingrese la duracion del viaje en minutos: "))

    total = tarifa_base + distancia_km * distancia_cliente + duracion_min * duracion_cliente
    total_km = total_km + distancia_cliente
    total_min = total_min + duracion_cliente
    total_final = total + total_final
    
    print(f"Su viaje tiene un total de {total} pesos")

    seguir = input("Desea realizar otro viaje: (S/N):")
    if seguir == "n" or seguir == "N" or seguir == "no" or seguir == "NO":
        
        break

print("las estadisticas de tus viajes durante el dia:")
print()
print(f"la cantidad de viajes: {contador}")
print()
print(f"Kilometros recorridos: {total_km}")
print()
print(f"minutos de viaje: {total_min}")
print()
print(f"El costo total de tus viajes es: {total_final}")
print()
print("Hasta pronto")


    

