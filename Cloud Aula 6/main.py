import requests
import json
from flask import Flask, jsonify

# --- ETAPA 1 e 2: Consumir API e Salvar em JSON ---

def buscar_e_salvar_dados():
    """
    Consome uma API pública (JSONPlaceholder) e salva os dados
    localmente em um arquivo 'dados.json'.
    """
    # 1. Consumir a API
    url = "https://jsonplaceholder.typicode.com/posts/1" # Usando o post de ID 1 como exemplo
    
    print("Iniciando busca de dados na API...")
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se houve erros na requisição
        
        # Converte a resposta em dicionário Python
        dados = resposta.json()
        print("Dados recebidos com sucesso!")

        # 2. Salvar o resultado em um arquivo JSON local
        with open('dados.json', 'w', encoding='utf-8') as arquivo:
            # json.dump() grava os dados no arquivo
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            
        print("Arquivo 'dados.json' salvo localmente.")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        return False

# --- ETAPA 3: Criar API Flask com rota /dados ---

# Cria a aplicação Flask
app = Flask(__name__)

@app.route('/dados')
def servir_dados():
    """
    Disponibiliza o conteúdo salvo em 'dados.json'
    """
    print("Requisição recebida na rota /dados")
    try:
        # Abre e lê o arquivo JSON salvo
        with open('dados.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
            
        # Retorna os dados usando jsonify (correto para Flask)
        return jsonify(dados)
        
    except FileNotFoundError:
        print("Erro: O arquivo 'dados.json' ainda não foi criado.")
        return jsonify({"erro": "Arquivo de dados não encontrado. Execute o script primeiro."}), 404
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return jsonify({"erro": str(e)}), 500

# --- Bloco de Execução Principal ---

if __name__ == '__main__':
    # Primeiro, executa a função para buscar e salvar os dados
    if buscar_e_salvar_dados():
        # Se os dados foram salvos com sucesso, inicia o servidor Flask
        print("\nIniciando o servidor Flask...")
        print("Acesse http://127.0.0.1:5000/dados no seu navegador.")
        app.run(debug=True)
    else:
        print("Servidor não iniciado. Falha ao obter dados da API.")