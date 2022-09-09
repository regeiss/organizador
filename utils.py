#===========================================================================================================================================
# -*- coding: utf-8 -*-  
# Arquivo: utils.py
# Versão: 1.0
# Última alteração: 09/09/2002 
# Propósito: programa utilitarios arquivos diretorios projeto1
# Autor: Roberto Edgar Geiss 
# Copyright:  
# Produto:  
# Observacoes: projeto1
# Parametros: 
# Detalhes especificos: Curso extensão UFRGS - Introdução ao Python
#===========================================================================================================================================
import os
import shutil

def make_dir(dir: str):
    if os.path.exists(dir) == False:
        os.mkdir(dir)

arquivos = os.listdir()

def move_file(direc: list):
    for arquivo in arquivos:
        if ".xls" in arquivo:
            shutil.move(arquivo, f"./planilhas/{arquivo}")
        elif ".doc" in arquivo:
            shutil.move(arquivo, f"./documentos/{arquivo}")
        elif ".docx" in arquivo:
            shutil.move(arquivo, f"./documentos/{arquivo}")

