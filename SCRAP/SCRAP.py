import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

def scrap_dolar():
    url = "https://www.lanacion.com.ar"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text()
    match = re.search(r'Dólar oficial \$([0-9,]+)', text)

    if match:
        dolar_oficial_str = match.group(1).replace(",", "")
        dolar_oficial_float = float(dolar_oficial_str) / 100 
        return dolar_oficial_float
    else:
        return None

def calculadora():
    try:
        precio_usd = float(input("Ingrese el precio en dólares: ")) 
        
        dolar_oficial = scrap_dolar()
        
        if dolar_oficial:
            print(f"Dólar Oficial: ${dolar_oficial:.2f}")
            
            precio_en_pesos = precio_usd * dolar_oficial
            precio_en_pesos *= 1.10  #Agrego 10% por posibles fluctuaciones

            IVA = 0.21
            IMPUESTO_PAIS = 0.08
            IMPUESTO_GANANCIAS = 0.30
            IIBB_CORDOBA = 0.03

            precio_final  = precio_en_pesos * (1 + IVA + IMPUESTO_PAIS + IMPUESTO_GANANCIAS + IIBB_CORDOBA)

            print(f"Valor a pagar: {precio_final:.2f}")
        else:
            print("Error.")
    
    except ValueError:
        print("Error.")

calculadora()