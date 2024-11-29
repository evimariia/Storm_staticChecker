import os
import argparse
from modules.lexical_analyzer import scan

def main():
    parser = argparse.ArgumentParser(description="Processa um arquivo de texto.") # Initialize parser
    parser.add_argument("file", help="Caminho do arquivo a ser processado") # Add argument file to the parse
    args = parser.parse_args() # Analyze args give in the CLI

    #openFile(args.file)
    scan(args.file)

if __name__ == "__main__":
    main()