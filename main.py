import os
import argparse
from modules.lexical_analyzer import alternate_scan, generateLexicalReport
from modules.symbol_table import generate_symbol_table_report
from modules.syntatic_analyzer import classify_atoms

def process_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Erro: O arquivo '{file_path}' não foi encontrado. Verifique o caminho e tente novamente.")
        return

    print(f"Processando o arquivo: {file_path}")
    alternate_scan(file_path)
    classify_atoms()
    generateLexicalReport(file_path)
    generate_symbol_table_report(file_path)
    print("Processamento concluído!")

def main():
    parser = argparse.ArgumentParser(description="Processa um arquivo de texto.")
    parser.add_argument("file", help="Caminho do arquivo a ser processado")
    args = parser.parse_args()  
    process_file(args.file)

if __name__ == "__main__":
    main()