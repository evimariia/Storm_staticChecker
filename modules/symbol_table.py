import os
import re

# Lista para armazenar a tabela de símbolos
symbol_table = []

# Função que processa o átomo identificado e insere na tabela de símbolos
def process_atom(atom, line_number):
    atom_type = classify_atom(atom)
    if atom not in reservedWordsAndSymbols.values() and atom_type != "Desconhecido":
        add_symbol_to_table(atom, atom_type, line_number)
    print(f"Átomo processado: {atom}, Tipo: {atom_type}")

# Função para classificar o átomo
def classify_atom(atom):
    if re.match(r'^"[^"]*"$', atom):  # Cadeia de caracteres
        return 'C01'
    elif re.match(r"^'[^']'$", atom):  # Caractere
        return 'C02'
    elif re.match(r'^[0-9]+$', atom):  # Número inteiro
        return 'C03'
    elif re.match(r'^[+-]?\d+(\.\d+)?$', atom):  # Número real
        return 'C04'
    elif atom in reservedWordsAndSymbols.values():  # Palavras reservadas e símbolos
        return next(key for key, value in reservedWordsAndSymbols.items() if value == atom)
    return 'Desconhecido'

# Adiciona um símbolo à tabela
def add_symbol_to_table(atom, atom_type, line_number):
    if not any(entry['lexeme'] == atom for entry in symbol_table):
        entry = {
            'lexeme': atom,
            'type': atom_type,
            'lines': [line_number]
        }
        symbol_table.append(entry)
    else:
        # Se o átomo já existir, atualiza as linhas em que aparece
        for entry in symbol_table:
            if entry['lexeme'] == atom and line_number not in entry['lines']:
                entry['lines'].append(line_number)

# Função para gerar o relatório da tabela de símbolos
def generate_symbol_table_report(file_path):
    base_name = os.path.basename(file_path).split('.')[0]
    filename = f"./results/{base_name}_symbol_table.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"RELATÓRIO DA TABELA DE SÍMBOLOS - {file_path}\n")
        f.write(f"{'Lexeme':<20} {'Type':<15} {'Lines'}\n")
        for entry in symbol_table:
            f.write(f"{entry['lexeme']:<20} {entry['type']:<15} {entry['lines']}\n")
    print(f"Relatório gerado em {filename}")
