# Use a imagem base Python
FROM python:3.11-alpine

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o código do servidor para o contêiner
COPY . /app

# Instale as dependências (se houver um arquivo requirements.txt)
RUN pip install flask && pip install requests

# Exponha a porta em que o servidor estará escutando
EXPOSE 8081

# Comando para iniciar o servidor
CMD ["python", "python_Server.py"]