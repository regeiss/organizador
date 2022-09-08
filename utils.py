import os
import shutil
# 

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

