from flask import Flask, Response, request
import requests

app = Flask(__name__)

# Endpoint para coletar métricas no formato Prometheus Exposition
@app.route('/metrics', methods=['GET'])
def get_metrics():
    # Faça uma solicitação ao servidor para obter as métricas JSON
    server_response = requests.get('http://pdfer-app:8080/files')

    if server_response.status_code == 200:
        # Traduza as métricas JSON em formato Prometheus Exposition
        json_metrics = server_response.json()
        prometheus_metrics = translate_to_prometheus(json_metrics)
        
        # Retorne as métricas no formato de texto simples
        return Response(prometheus_metrics, content_type='text/plain')
    else:
        return 'Erro ao recuperar métricas do servidor', 500

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
