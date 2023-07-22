# Projeto de Extração de Informações de Notas Fiscais

Este é um projeto que visa extrair informações de arquivos XML de notas fiscais e criar uma tabela em formato Excel contendo essas informações. O projeto é útil para empresas que precisam processar um grande volume de notas fiscais e desejam automatizar o processo de extração de informações.

## Executando o Projeto

Para executar o projeto, siga os passos abaixo:

1. Certifique-se de ter as seguintes bibliotecas instaladas no seu ambiente Python:
   - `xmltodict`: utilizada para transformar o arquivo XML em um dicionário
   - `pandas`: utilizada para criar a tabela em formato Excel

2. Crie uma pasta chamada "nfs" e coloque os arquivos XML das notas fiscais nessa pasta. Certifique-se de que os arquivos XML seguem a estrutura correta de notas fiscais.

3. Execute o código fornecido no arquivo Python. O código percorrerá os arquivos XML na pasta "nfs", extrairá as informações relevantes de cada nota fiscal e armazenará essas informações em uma tabela.

4. Após a execução do código, uma tabela em formato Excel será criada e salva em um arquivo chamado "NotasFiscais.xlsx" na pasta "tabelas". Essa tabela conterá as informações extraídas das notas fiscais.

## Licença

Este projeto está disponível sob a licença MIT. A licença MIT é uma licença de código aberto amplamente utilizada e permite que empresas usem, modifiquem e distribuam o código deste projeto para necessidades internas.

## Considerações Finais

Esperamos que este projeto seja útil para empresas que desejam automatizar o processo de extração de informações de notas fiscais. A utilização de tecnologias como `xmltodict` e `pandas` simplifica o processo de manipulação e processamento de arquivos XML e criação de tabelas.