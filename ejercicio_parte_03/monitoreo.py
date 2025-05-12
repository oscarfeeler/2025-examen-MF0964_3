import psutil

def mostrar_numero_procesos():
    num_procesos = len(psutil.pids())
    print(f"El número de procesos en ejecución es: {num_procesos}")
    
def mostrar__