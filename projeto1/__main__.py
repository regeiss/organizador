

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