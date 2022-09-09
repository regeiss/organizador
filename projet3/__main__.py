#===========================================================================================================================================
# -*- coding: utf-8 -*-  
# Arquivo: __main__.py
# Versão: 1.0
# Última alteração: 09/09/2002 
# Propósito: programa main projeto3 - ler pagina web e gravara arquivo
# Autor: Roberto Edgar Geiss 
# Copyright:  
# Produto:  
# Observacoes: projeto3
# Parametros: 
# Detalhes especificos: Curso extensão UFRGS - Introdução ao Python
#===========================================================================================================================================
import requests 

def page_reader(endereco: str) -> requests.models.Response:
    pagina = requests.get(endereco)
    return pagina 

def grava_pagina_web(resposta: requests.models.Response) -> None:
    arquivo = open('politica.html','wb')
    for texto in resposta.iter_content():
        arquivo.write(texto)
    arquivo.close()

def main():
    endereco = 'https://g1.globo.com/politica/'
    politica = page_reader(endereco)
    grava_pagina_web(politica)

if __name__ == "__main__":
    main() 
# eof
