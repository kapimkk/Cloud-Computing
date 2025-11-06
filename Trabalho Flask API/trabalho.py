import requests

def buscar_dados_github(usuario, repo):
    """Busca dados de um repositório específico no GitHub."""
    
    # URL da API do GitHub para repositórios
    url = f"https://api.github.com/repos/{usuario}/{repo}"
    
    print(f"Buscando dados de: {url}")
    
    try:
        # Faz a requisição GET
        resposta = requests.get(url)
        
        # Verifica se a requisição foi bem-sucedida (código 200)
        resposta.raise_for_status()
        
        # Converte a resposta JSON em um dicionário Python
        dados = resposta.json()
        
        # Exibe os dados solicitados
        print("\n--- Dados do Repositório ---")
        print(f"Nome: {dados['name']}")
        print(f"Descrição: {dados['description']}")
        print(f"Estrelas (Stargazers): {dados['stargazers_count']}")
        print("----------------------------")
        
    except requests.exceptions.HTTPError as errh:
        print(f"Erro HTTP: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Erro de Conexão: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Erro de Timeout: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Erro na Requisição: {err}")

# --- Execução do Script ---
if __name__ == "__main__":
    # Exemplo: Buscando o repositório 'cpython' do usuário 'python'
    buscar_dados_github('python', 'cpython')