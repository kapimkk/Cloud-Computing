import requests

def get_clima(cidade, latitude, longitude):
    """Busca a temperatura e velocidade do vento para uma coordenada."""
    
    # URL da API Open-Meteo
    url = "https://api.open-meteo.com/v1/forecast"
    
    # Parâmetros da API
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m" # Pede temp. e vento atuais
    }
    
    print(f"Buscando clima para {cidade}...")
    
    try:
        resposta = requests.get(url, params=params)
        resposta.raise_for_status()
        
        dados = resposta.json()
        
        # Extrai os dados atuais
        temp = dados['current']['temperature_2m']
        vento = dados['current']['wind_speed_10m']
        
        # Extrai as unidades
        temp_unit = dados['current_units']['temperature_2m']
        vento_unit = dados['current_units']['wind_speed_10m']
        
        print(f"--- Clima em {cidade} ---")
        print(f"Temperatura: {temp}{temp_unit}")
        print(f"Velocidade do Vento: {vento}{vento_unit}")
        print("-------------------------\n")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar clima para {cidade}: {e}")

# --- Execução do Script ---
if __name__ == "__main__":
    # Coordenadas de Curitiba
    get_clima("Curitiba", -25.43, -49.27)
    
    # Outra cidade (Exemplo: São Paulo)
    get_clima("São Paulo", -23.55, -46.64)