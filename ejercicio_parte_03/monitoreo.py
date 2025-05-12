import psutil

def mostrar_numero_procesos():
    num_procesos = len(psutil.pids())
    print(f"El número de procesos en ejecución es: {num_procesos}")
    if num_procesos >= 100:
        print("ALERTA: demasiados procesos")
    
def mostrar_nombres_procesos():
    procesos = []
    for i in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            procesos.append(i.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue   
    procesos_ordenados = sorted(procesos, key=lambda x: x['cpu_percent'], reverse=True)[:3]
    print("Los 3 procesos que más CPU consumen son:")
    for p in procesos_ordenados:
        print(f"PID: {p['pid']}, Nombre: {p['name']}, CPU: {p['cpu_percent']}%")

        
mostrar_numero_procesos()
mostrar_nombres_procesos()