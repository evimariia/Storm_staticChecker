import os
import re

symbolTable = [
    ['atom', 'code', 'line', 'type', 'qtdeBeforetrunk', 'qtdeAfterTrunk', 0]
]

indice = 0

divider = "==============================================\n"
header = """Equipe 04: os caras do momento.
            Componentes:
            \n
            """

def add_symbol_to_table(atom, code, line_number, atom_type, qtdeBeforeTrunk, qtdeAfterTrunk):
    global indice
    indice += 1
    new_entry = [
            atom,
            code,
            line_number, 
            atom_type,
            qtdeBeforeTrunk, 
            qtdeAfterTrunk,
            indice
        ]
    symbolTable.append(new_entry)

def atom_in_table(atom):
     for entry in symbolTable:
        if entry and entry[0] == atom:
            return True
        
def update_atom_code(atom, code):
    for entry in symbolTable:
        if entry and entry[0] == atom:
                entry[1] = code
                break
        
def update_atom_type(atom, atom_type):
    for entry in symbolTable:
        if entry and entry[0] == atom:
                entry[3] = atom_type
                break

def update_atom_lines(atom, line_number):
    for entry in symbolTable:
        if entry and entry[0] == atom:
            if line_number not in entry[2] and len(entry[2]) <= 5:
                entry[2] = line_number

def searchSymbol(symbol, cod):    
    found = 0
    for code in symbolTable:
        if cod[0] == "C" and code[0] == cod and code[0] == symbol:
            found = 1
            break
        elif code[0] == symbol and code[1] == cod:
             found = 1
             break

    if found == 1:
         return True
    else:
         return False

def getIndex(symbol, code):
    for entry in symbolTable:
        if (entry[0] == symbol and entry[1] == code):
            return entry[6]
        
def getCode(index):
    for entry in symbolTable:
        if(entry[6] == index):
            return entry[1]
    
def generate_symbol_table_report(file_path):
    divider = "-" * 50 +"\n" 
    base_name = os.path.basename(file_path).split('.')[0]
    filename = f"./results/{base_name}_symbol_table.TAB"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"{header}\nRELATÓRIO DA TABELA DE SÍMBOLOS - {file_path}\n\n")
        for entry in symbolTable:
            if entry[6] > 0:
                f.write(f"""\nEntrada: {entry[6]}, Código: {entry[1]}, Lexeme: {entry[0]}
Pré-truncagem: {entry[4]}, Pós-truncagem: {entry[5]}
Tipo: {entry[3]}, Linhas: {entry[2]}\n{divider}""")
            else:
                continue
    print(f"Relatório gerado em {filename}")
