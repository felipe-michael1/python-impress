import cups

def imprimir(texto, impressora=None):
    conn = cups.Connection()
    impressoras = conn.getPrinters()

    # Se nenhum nome de impressora for fornecido, usa a primeira disponível
    if impressora is None:
        impressora = list(impressoras.keys())[0]

    if impressora not in impressoras:
        raise ValueError(f"Impressora '{impressora}' não encontrada.")

    # Prepara os dados para impressão
    dados = texto.encode('utf-8')

    # Realiza a impressão
    job_id = conn.printFile(impressora, 'impressao.txt', 'Documento de Impressao', {'cpi': '12', 'lpi': '8', 'raw': 'on', 'rawOption': 'nofilter'}, dados)

    print(f"Documento enviado para impressora '{impressora}' com ID: {job_id}")

# Exemplo de uso:
texto_para_imprimir = """
Teste de impressao utilizando Python.
Este é um exemplo simples de como imprimir um texto.
"""

try:
    imprimir(texto_para_imprimir)
except Exception as e:
    print(f"Erro ao imprimir: {e}")
