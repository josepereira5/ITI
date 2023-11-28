import threading
import requests
import time
import random

def make_constant_get_requests():
    while True:
        server_response = requests.get('http://pdfer-app::8080/files')

def make_constant_post_requests():
    while True:
        fileName = criar_arquivo_com_nome_aleatorio()
        data = {
            "key": "1234123412341234",
            "length": 200,
            "fileName": fileName
        }
        
        server_response = requests.post("http://pdfer-app:8080/files", json=data)

def make_constant_getFile_requests():
    while True:
        data = {
            "key": "1234123412341234",
            "fileName": "fileName"
        }
        server_response = requests.get("http://pdfer-app:8080/files/fileName", json=data)

        


def gerar_nome_aleatorio(silabas, quantidade):
    nomes_gerados = []
    
    for _ in range(quantidade):
        nome = ''.join(random.choice(silabas) for _ in range(random.randint(2, 4)))
        nomes_gerados.append(nome.capitalize())
    
    return nomes_gerados

def criar_arquivo_com_nome_aleatorio():
    silabas_disponiveis = ['a', 'e', 'i', 'o', 'u', 'ba', 'ri'  'be', 'bi', 'bo', 'bu', 'da', 'de', 'di', 'do', 'du']
    
    nome_aleatorio = gerar_nome_aleatorio(silabas_disponiveis, 1)[0]
    
    return nome_aleatorio
    
def main():
    """
        print("Escolha uma opção:")
        print("1. Opção 1")
        print("2. Opção 2")
        print("3. Opção 3")
        
        opcao = int(input("Insira o número da opção: "))
        threads = int(input("Insira o número de threads a criar: "))
"""
    opcao = 2
    threads = 0
            
    if opcao == 1:
        for _ in range(threads):
            thread = threading.Thread(target=make_constant_get_requests)
            thread.daemon = True
            thread.start()
    
    elif opcao == 2:
        for _ in range(threads):
            thread = threading.Thread(target=make_constant_post_requests)
            thread.daemon = True
            thread.start()

    elif opcao == 3:
        data = {
        "key": "1234123412341234",
        "length": 200,
        "fileName": "fileName"
        }
        server_response = requests.post("http://pdfer-app:8080/files", json=data)
        for _ in range(threads):
            thread = threading.Thread(target=make_constant_getFile_requests)
            thread.daemon = True
            thread.start()

    else:
        print("Opção inválida. Escolha uma opção válida.")

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
