#===========================================================================================================================================
# -*- coding: utf-8 -*-  
# Arquivo:  .py
# Versão: 1.0
# Última alteração:  
# Propósito: 
# Autor: Roberto Edgar Geiss 
# Copyright:  
# Produto:  
# Observacoes:  
# Parametros: 
# Detalhes especificos: 
#===========================================================================================================================================
from openpyxl import Workbook 
import os, sys, time, re

localTime = time.asctime( time.localtime(time.time()) )  
strHora = "Gerado em : " +  localTime  

def cria_wb(filename: str) -> Workbook:
    wb = Workbook()
    return wb

def cria_ws(planilha: str, pasta: Workbook) -> None:
    pasta.active
    pasta.create_sheet(planilha)


