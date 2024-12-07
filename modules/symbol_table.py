import os
import re

symbolTable = [
    ['atom', 'code', 'line', 'type', 'qtdeBeforetrunk', 'qtdeAfterTrunk']
]

indice = 0

def add_symbol_to_table(atom, code, line_number, atom_type, qtdeBeforeTrunk, qtdeAfterTrunk):
    '''for entry in symbolTable:
        if entry and entry[0] == atom:
            return'''
    
    #if (searchSymbol(atom, code)==False):
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
    #else:
        #update_atom_lines(atom, line_number)

def atom_in_table(atom):
     for entry in symbolTable:
        if entry and entry[0] == atom:
            return True

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
    
def generate_symbol_table_report(file_path):
    #esse indice é uma solução temporária, deveria estar no addSymbol
    #index=0
    base_name = os.path.basename(file_path).split('.')[0]
    filename = f"./results/{base_name}_symbol_table.TAB"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"{header}\nRELATÓRIO DA TABELA DE SÍMBOLOS - {file_path}\n\n")
        #f.write(f"{'Lexeme':<20} {'Code':<15} {'Lines'} {'Type'} {'BeforeTrunk'} {'AfterTrunk'}\n")
        for entry in symbolTable:
            if (entry[6] > 0):
                f.write(f"""Entrada: {entry[6]}, Código: {entry[1]}, Lexeme: {entry[0]}
Pré-truncagem: {entry[4]}, Pós-truncagem: {entry[5]}
Tipo: {entry[3]}, Linhas: {entry[2]}\n{divider}""")
            #index +=1
    print(f"Relatório gerado em {filename}")
        
file_path = r"C:\Users\Bruno\Storm_staticChecker\teste.242"
#add_symbol_to_table('programa', 'A17', [1,1,2], "ReservedWord", 8, 8)
#add_symbol_to_table('samplix', 'C01', [2,2,2], "ConsCadeia", 7, 7)
#update_atom_lines('samplix', 3)
generate_symbol_table_report(file_path)
