from flask import Flask, Response, request
import requests
import random
import os
import logging 
import threading
import time

global ola

ola=1

def make_constant_getFile_requests():
    while True:
        data = {
            "key": "1234123412341234",
            "fileName": "fileName"
        }
        server_response = requests.get("http://pdfer-app:8080/files/fileName", json=data)


def make_constant_get_requests():
    while True:
        server_response = requests.get('http://pdfer-app:8080/files')
        
def make_constant_post_requests():
    while True:
        fileName = criar_arquivo_com_nome_aleatorio()
        data = {
            "key": "1234123412341234",
            "length": 200,
            "fileName": fileName
        }
        
        server_response = requests.post("http://pdfer-app:8080/files", json=data)


def gerar_nome_aleatorio(silabas, quantidade):
    nomes_gerados = []
    
    for _ in range(quantidade):
        nome = ''.join(random.choice(silabas) for _ in range(random.randint(2, 4)))
        nomes_gerados.append(nome.capitalize())
    
    return nomes_gerados

def criar_arquivo_com_nome_aleatorio():
    silabas_disponiveis = ['a', 'e', 'i', 'o', 'u', 'ba', 'be', 'bi', 'bo', 'bu', 'da', 'de', 'di', 'do', 'du']
    
    nome_aleatorio = gerar_nome_aleatorio(silabas_disponiveis, 1)[0]
    
    return nome_aleatorio

app = Flask(__name__)

# Endpoint para coletar métricas no formato Prometheus Exposition
@app.route('/metrics', methods=['GET'])
def get_metrics():
    global ola
    # Configuração básica do logging
    logging.basicConfig(level=logging.INFO)  # ou logging.DEBUG para incluir mensagens de debug

    # Faça uma solicitação ao servidor para obter as métricas JSON (GET)
    """
    if ola==1:
        ola=2
        for _ in range(1000000000):
            thread = threading.Thread(target=make_constant_get_requests)
            thread.daemon = True
            thread.start()

    server_response = requests.get('http://pdfer-app:8080/files')
    if server_response.status_code == 200:
        # Traduza as métricas JSON em formato Prometheus Exposition
        json_metrics = server_response.json()
        prometheus_metrics = translate_to_prometheus(json_metrics)
        
        # Retorne as métricas no formato de texto simples
        return Response(prometheus_metrics, content_type='text/plain')
    else:
        return 'Erro ao recuperar métricas do servidor', 500
    """
    #Post
    
    if ola==1:
        ola=2
        for _ in range(2500):
            thread = threading.Thread(target=make_constant_post_requests)
            thread.daemon = True
            thread.start()

    fileName = criar_arquivo_com_nome_aleatorio()
    data = {
        "key": "1234123412341234",
        "length": 200,
        "fileName": fileName
    }
    
    server_response = requests.post("http://pdfer-app:8080/files", json=data)
    
    if server_response.status_code == 201:
        logging.info("Arquivo criado e encriptado com sucesso!")
        json_metrics = server_response.json()
        prometheus_metrics = translate_to_prometheus(json_metrics)
        logging.info(prometheus_metrics)
        return Response(prometheus_metrics, content_type='text/plain')
    else:
        print(f"Erro: {server_response.status_code}")




    #Get Files
"""
    if ola==1:
        ola=2
        data = {
        "key": "1234123412341234",
        "length": 200,
        "fileName": "fileName"
        }
        server_response = requests.post("http://pdfer-app:8080/files", json=data)
        for _ in range(10000):
            thread = threading.Thread(target=make_constant_getFile_requests)
            thread.daemon = True
            thread.start()

    
    data = {
        "key": "123412data = {
        "key": "1234123412341234",
        "length": 200,
        "fileName": "fileName"
        }
        server_response = requests.post("http://pdfer-app:8080/files", json=data)3412341234"
    }
    server_response = requests.get("http://pdfer-app:8080/files/fileName", json=data)
    if server_response.status_code == 200:
        json_metrics = server_response.json()
        prometheus_metrics = translate_to_prometheus(json_metrics)
        logging.info(prometheus_metrics)
        return Response(prometheus_metrics, content_type='text/plain')
    else:
        print(f"Erro: {server_response.status_code}")
"""

def translate_to_prometheus(json_metrics):
    prometheus_lines = []

    if 'metrics' in json_metrics:
        metrics = json_metrics['metrics']
        
        # Se a métrica 'unit' estiver presente, armazene-a como rótulo
        unit = metrics.get('unit', '')
        
        # Iterar sobre todas as métricas no JSON
        for metric_name, metric_value in metrics.items():
            # Ignore a métrica 'unit' no loop de iteração
            if metric_name == 'unit':
                continue
            
            # Adicione a métrica traduzida à lista de linhas Prometheus
            if unit:
                prometheus_lines.append(f'files_metric{{unit="{unit}", operation="{metric_name}"}} {metric_value}')
            else:
                prometheus_lines.append(f'files_metric{{operation="{metric_name}"}} {metric_value}')

    # Combine todas as linhas em uma única string
    prometheus_metrics = '\n'.join(prometheus_lines)

    return prometheus_metrics


  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
