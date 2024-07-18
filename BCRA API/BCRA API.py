import requests

# Añadir Token de https://estadisticasbcra.com/api/registracion
token = " "

endpoint_usd_of = "usd_of"

def get_data(endpoint):
    url = f"https://api.estadisticasbcra.com/{endpoint}"
    headers = {
        "Authorization": f"BEARER {token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        if response.status_code == 200:
            data_json = response.json()
            return data_json
        else:
            print(f"Error al obtener datos desde la API ({endpoint}), código de estado: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud HTTP: {e}")
        return None

def calculadora():
    try:
        precio_usd = float(input("Ingrese el precio en dólares: ")) 
        # Ingresar con ".", no con ","
        
        usd_of_data = get_data(endpoint_usd_of)
        if usd_of_data:
            if isinstance(usd_of_data, list) and len(usd_of_data) > 0:
                ultimo_valor_dolar_oficial = usd_of_data[-1]['v']

                print(f"Dolar Oficial: {ultimo_valor_dolar_oficial}")
                
                precio_en_pesos = precio_usd * ultimo_valor_dolar_oficial
                precio_en_pesos *= 1.10  
                
                IVA = 0.21
                IMPUESTO_PAIS = 0.08
                IMPUESTO_GANANCIAS = 0.30
                IIBB_CORDOBA = 0.03
                
                precio_final = precio_en_pesos * (1 + IVA + IMPUESTO_PAIS + IMPUESTO_GANANCIAS + IIBB_CORDOBA)
                
                print(f"Valor a pagar: {precio_final:.2f}")
            else:
                print("Error")
        else:
            print("Error")
    
    except ValueError:
        print("Error")

calculadora()