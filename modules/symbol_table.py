import os
import re
from lexical_analyzer import reservedWordsAndSymbols

symbolTable = [
    ['atom', 'code', 'line', 'type', 'qtdeBeforetrunk', 'qtdeAfterTrunk']
]

def add_symbol_to_table(atom, code, line_number, atom_type, qtdeBeforeTrunk, qtdeAfterTrunk):
    for entry in symbolTable:
        if entry and entry[0] == atom:
            return
    
    new_entry = [
        atom,
        code,
        [line_number], 
        atom_type,
        qtdeBeforeTrunk, 
        qtdeAfterTrunk
    ]
    symbolTable.append(new_entry)

def update_atom_code(atom, code):
    for entry in symbolTable:
        if entry and entry[0] == atom:
                entry[1] = code

def update_atom_type(atom, atom_type):
    for entry in symbolTable:
        if entry and entry[0] == atom:
                entry[3] = atom_type

def update_atom_lines(atom, line_number):
    for entry in symbolTable:
        if entry and entry[0] == atom:
            if line_number not in entry[2]:
                entry[2] = line_number

def generate_symbol_table_report(file_path):
    base_name = os.path.basename(file_path).split('.')[0]
    filename = f"./results/{base_name}_symbol_table.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"RELATÓRIO DA TABELA DE SÍMBOLOS - {file_path}\n")
        f.write(f"{'Lexeme':<20} {'Type':<15} {'Lines'}\n")
        for entry in symbolTable:
            f.write(f"{entry['lexeme']:<20} {entry['type']:<15} {entry['lines']}\n")
    print(f"Relatório gerado em {filename}")
