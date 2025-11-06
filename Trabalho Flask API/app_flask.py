from flask import Flask, jsonify
import json

# Inicializa a aplicação Flask
app = Flask(__name__)

# --- Definição das Rotas ---

@app.route('/')
def home():
    """Rota principal (homepage)."""
    return "Bem-vindo à API de Alunos e Cursos!"

@app.route('/alunos')
def get_alunos():
    """
    Rota para ler e retornar os dados do arquivo 'alunos.json'.
    Simula o consumo de dados locais (como um "banco de dados" JSON).
    """
    try:
        with open('alunos.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        return jsonify(dados)
    
    except FileNotFoundError:
        return jsonify({"erro": "Arquivo 'alunos.json' não encontrado"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/saudacao/<nome>')
def saudacao(nome):
    """Rota dinâmica que recebe um nome."""
    return jsonify({
        "mensagem": f"Olá, {nome}!",
        "instrucao": "Você usou uma rota dinâmica com seu nome."
    })

@app.route('/curso/<curso>')
def get_curso(curso):
    """Rota dinâmica que recebe um nome de curso."""
    return jsonify({
        "curso_consultado": curso,
        "mensagem": f"Buscando informações para o curso de: {curso.upper()}"
    })

# --- Execução do Servidor ---
if __name__ == '__main__':
    """
    Roda o servidor Flask em modo 'debug'
    Acesse em: http://127.0.0.1:5000
    """
    print("Servidor Flask rodando em http://127.0.0.1:5000")
    print("Acesse as rotas: / , /alunos , /saudacao/seu-nome , /curso/seu-curso")
    app.run(debug=True)