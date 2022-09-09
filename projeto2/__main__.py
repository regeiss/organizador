#===========================================================================================================================================
# -*- coding: utf-8 -*-  
# Arquivo: __main__.py
# Versão: 1.0
# Última alteração: 09/09/2002 
# Propósito: programa main projeto1
# Autor: Roberto Edgar Geiss 
# Copyright:  
# Produto:  
# Observacoes: projeto1
# Parametros: 
# Detalhes especificos: Curso extensão UFRGS - Introdução ao Python
#===========================================================================================================================================
import random 
from openpyxl import Workbook
import gera_wb

def main():

    rel_planilhas = ['receitas','despesas','resultado']
    pasta = gera_wb.cria_wb('orcamento.xls')
    pasta.active

    for planilha in lista_planilhas:
        gera_wb.cria_ws(pasta)

if __name__ == "__main__":
    main() 
# eof
