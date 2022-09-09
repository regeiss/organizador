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
import os
import shutil
import utils

def main():

    arquivos = os.listdir()
    for diretorio in ['documentos', 'planilhas']:
        utils.make_dir(diretorio)
    utils.move_file(arquivos)

if __name__ == "__main__":
    main() 
# eof
