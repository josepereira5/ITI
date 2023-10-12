# Use a imagem base adequada do Go (substitua a versão desejada)
FROM ubuntu

# Crie um diretório de trabalho no contêiner
WORKDIR /server

# Copie o arquivo "pdfer" para o diretório de trabalho no contêiner
COPY pdfer .

# Defina as permissões de execução para o arquivo "pdfer"
RUN chmod +x pdfer && mkdir store

# Defina o comando de inicialização do contêiner para executar o "pdfer"
CMD ["./pdfer"]
