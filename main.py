import xmltodict
import os
import pandas as pd

def pegar_infos(nome_arquivo, valores): # função para pegar as informações do arquivo
    
    # print(f"Arquivo: {nome_arquivo}") # imprime o nome do arquivo
    
    with open(f"nfs/{nome_arquivo}", "rb") as arquivo_xml: # abre o arquivo xml
        
        dict_arquivo = xmltodict.parse(arquivo_xml) # transforma o arquivo xml em um dicionário
        
        # print(json.dumps(dict_arquivo, indent=4)) 
        
        if "NFe" in dict_arquivo: # se tiver a tag NFe no arquivo, pega as informações da nota fiscal
            infos_nf = dict_arquivo["NFe"]['infNFe'] # pega as informações da nota fiscal
        else: # se não tiver a tag NFe no arquivo, pega as informações da nota fiscal
            
            infos_nf = dict_arquivo["nfeProc"]["NFe"]['infNFe']  # pega as informações da nota fiscal
            
        numero_nota = infos_nf["ide"]["nNF"] # pega o número da nota fiscal
        empresa_emissora = infos_nf['emit']['xNome']
        nome_cliente = infos_nf["dest"]["xNome"]
        endereco = infos_nf["dest"]["enderDest"]["xLgr"]
        if "vol" in infos_nf["transp"]: # se tiver a tag vol no arquivo, pega as informações do volume
            peso = infos_nf["transp"]["vol"]["pesoB"]
        else:
            peso = "Não informado"
        
        valores.append([numero_nota, empresa_emissora, nome_cliente, endereco, peso]) # adiciona os valores na lista de valores
            
lista_arquivos = os.listdir("nfs") # lista os arquivos da pasta nfs

colunas = ["numero_nota", "empresa_emissora", "nome_cliente", "endereco", "peso"] # cria uma lista com o nome das colunas
valores = [] # cria uma lista vazia para armazenar os valores

for arquivo in lista_arquivos: # para cada arquivo na lista de arquivos
    pegar_infos(arquivo, valores) # chama a função pegar_infos passando o nome do arquivo
    
tabela = pd.DataFrame(columns=colunas, data=valores) # cria uma tabela com os valores
tabela.to_excel(f"tabelas/NotasFiscais.xlsx", index=False) # salva a tabela em um arquivo excel