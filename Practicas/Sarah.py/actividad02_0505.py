def solicitar_datos_estudiante():
    nombre = input("ingrese el nombre del estudiante: ")
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"ingrese la nota {i} (de 0 a 5): "))
                if 0 <= nota <= 5:
                    notas.append(nota)
                    break
                else:
                       print("la nota debe estar entre 0 a 5.")
            except ValueError:
                print("ingrese una nota valida.")
        return nombre, notas
    def calcular_promedio (notas):
        return sum(notas) / len(notas)
    def mostrar_resultado(nombre, promedio):
        estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"
        print(f"{nombre} tiene un promedio de {promedio:.2f} y ha {estado}")
    def main():
        try:
            cantidad = int(input("¿cuantos estudiantes desea ingresar?"))
            for _ in range (cantidad):
                nombre, notas = solicitar_datos_estudiante()
                promedio = calcular_promedio (notas)
                mostrar_resultado(nombre, promedio)
        except ValueError:
            print("ingrese un numero valido de estudiantes")
    if __name__ == "_main_":
        main()


"""num_estudiantes = int(input("ingrese el numero de estudiantes a consultar: "))
        if num_estudiantes <= 0:
            print("el numero de estudiantes debe ser mayor que 0")
        return
    except ValueError:
        print("ingrese un numero valido de estudiantes")
        return
    for i in range (num_estudiantes):
          print(f"estudiante {i + 1}: ")
          nombre, notas = solicitar_datos_estudiante()
          promedio = calcular_promedio(notas)
          mostrar_resultado(nombre, promedio)
          if __name__ == "_main_":
              main()"""

        