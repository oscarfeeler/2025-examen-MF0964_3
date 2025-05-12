import requests

def comprobar_estado():
    try:
        respuesta = requests.get("https://api.ejemplo.com/estado")
        if respuesta.status_code == 200:
            return "OK"
        else:
            return "ERROR"
    except requests.exceptions.RequestException:
        return "FALLO DE CONEXIÓN"
    
    