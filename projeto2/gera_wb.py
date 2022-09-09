#===========================================================================================================================================
# -*- coding: utf-8 -*-  
# Arquivo:  gera_wb.py
# Versão: 1.0
# Última alteração:  09/09/2022
# Propósito: programa main projeto2 - insere sheets em planilha - utilitario
# Autor: Roberto Edgar Geiss 
# Copyright:  
# Produto:  
# Observacoes: projeto2
# Parametros: 
# Detalhes especificos: Curso extensão UFRGS - Introdução ao Python
#===========================================================================================================================================
from openpyxl import Workbook 


def cria_wb(filename: str) -> Workbook:
    wb = Workbook()
    return wb

def cria_ws(planilha: str, pasta: Workbook) -> None:
    pasta.active
    pasta.create_sheet(planilha)

