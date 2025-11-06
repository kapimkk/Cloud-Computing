import json

def salvar_e_ler_dados_alunos():
    """
    Cria uma estrutura de dados de alunos, salva em 'alunos.json'
    e depois lê o arquivo de volta.
    """
    
    # 1. Dados dos Alunos (exemplo)
    dados_alunos = {
        "total_alunos": 2,
        "alunos": [
            {"id": 1, "nome": "Ana Silva", "curso": "ADS"},
            {"id": 2, "nome": "Bruno Costa", "curso": "Ciência de Dados"}
        ]
    }
    
    arquivo_nome = 'alunos.json'
    
    # 2. Salvar dados em JSON
    try:
        with open(arquivo_nome, 'w', encoding='utf-8') as f:
            # 'dump' escreve o dicionário no arquivo
            json.dump(dados_alunos, f, indent=4, ensure_ascii=False)
        
        print(f"Dados salvos com sucesso em '{arquivo_nome}'!")
    
    except IOError as e:
        print(f"Erro ao salvar o arquivo: {e}")

    # 3. Ler dados do JSON local
    try:
        with open(arquivo_nome, 'r', encoding='utf-8') as f:
            # 'load' lê o arquivo e converte para dicionário
            dados_lidos = json.load(f)
            
        print(f"\nLendo dados de '{arquivo_nome}':")
        print("---------------------------------")
        print(json.dumps(dados_lidos, indent=2, ensure_ascii=False)) # 'dumps' formata para printar
        print("---------------------------------")
        print("Leitura concluída com sucesso!")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_nome}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{arquivo_nome}' não é um JSON válido.")
    except IOError as e:
        print(f"Erro ao ler o arquivo: {e}")

# --- Execução do Script ---
if __name__ == "__main__":
    salvar_e_ler_dados_alunos()