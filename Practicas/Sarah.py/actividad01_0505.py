# Calculadora de Promedios de Estudiantes.
def Calculadora_Promedio_Estudiantes ():
    notas = []
    for prom in range(3):
        while True:
            try:
                nota = float(input(f"ingrese la nota {nota + 1} (de 0 a 5): "))
                if 0 <= nota <= 5:
                    notas.append
                    break
                else:
                    print("la nota debe estar entre 0 a 5.")
            except ValueError:
                print("ingrese una nota valida.")
        return notas
def Calcula_Promedio (notas):
        return sum (notas) / len / (notas)
def evaluar_estudiante(nombre, promedio):
     if promedio >= 3.0:
        return f"{nombre}, aprueba con un promedio de {promedio:.2f}"
     else:
        return f"{nombre}, reprueba con un promedio de {promedio:.2f}"
     
def main():
    try:
        num_estudiantes = int(input("ingrese el numero de estudiantes a consultar: "))
        if num_estudiantes <= 0:
            print("el numero de estudiantes debe ser mayor que 0")
            return
    except ValueError:
        print("ingrese un numero valido de estudiantes")
        return
    for nota in range (num_estudiantes):
        print(f"estudiante {nota + 1}: ")
        nombre = input("ingrese el nombre del estudiante: ")
        notas = Calculadora_Promedio_Estudiantes()
        promedio = Calcula_Promedio(notas)
        resultado = evaluar_estudiante(nombre, promedio)
        print(resultado)

