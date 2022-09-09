#===========================================================================================================================================
# -*- coding: utf-8 -*-  
# Arquivo: __main__.py
# Versão: 1.0
# Última alteração: 09/09/2002 
# Propósito: programa main projetofinal - ler pdados abertos TCE
# Autor: Roberto Edgar Geiss 
# Copyright:  
# Produto:  
# Observacoes: projeto3
# Parametros: 
# Detalhes especificos: Curso extensão UFRGS - Introdução ao Python
#===========================================================================================================================================
import requests 
import csv 
import os 

def csv_reader(endereco: str) -> None:
    with requests.Session() as sessao:
       csv_baixado = sessao.get(endereco)

    conteudo_decod = csv_baixado.content.decode('utf-8')
    cr = csv.reader(conteudo_decod.splitlines(), delimiter=',')
    
    with open('balancete.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerows(cr)

def main():
    endereco = 'http://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2022.csv'
    dados = csv_reader(endereco)

if __name__ == "__main__":
    main() 
# eof
