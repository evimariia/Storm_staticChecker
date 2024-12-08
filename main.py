import os
import argparse
from modules.lexical_analyzer import alternate_scan, generateLexicalReport
from modules.symbol_table import generate_symbol_table_report
from modules.syntatic_analyzer import classify_atoms

def main():
    '''parser = argparse.ArgumentParser(description="Processa um arquivo de texto.") # Initialize parser
    parser.add_argument("file", help="Caminho do arquivo a ser processado") # Add argument file to the parse
    args = parser.parse_args() # Analyze args give in the CLI'''

    file_path = r"C:\Users\evila\OneDrive\Documentos\teste1.242"
    alternate_scan(file_path)
    classify_atoms()
    generateLexicalReport(file_path)
    generate_symbol_table_report(file_path)

if __name__ == "__main__":
    main()