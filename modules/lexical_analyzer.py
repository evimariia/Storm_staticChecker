from modules.symbol_table import add_symbol_to_table, atom_in_table, update_atom_lines, getIndex
import os
import re

global list_atoms
list_atoms = {}

divider = "==============================================\n"
header = """Equipe 04: os caras do momento.
            Componentes:
            Bruno da Costa Sales, bruno.sales@aln.senaicimatec.edu.br, (71)99650-1212
            Évila Maria de Souza Carneiro, evila.carneiro@aln.senaicimatec.edu.br, (71)
            Gabriel Batista Reis, gabriel.b@aln.senaicimatec.edu.br, o memso de samplix
            João Victor Borges Lima, joao.l@aln.senaicimatec.edu.br, (71)4002-8922\n
            """

LexReport = [
    ['header', 'atom', 'code', 'symbolTableIndex', 'line']
]

validTokens = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '_', '$', '.', "'", '"', ' ', 
    '%', '(', ')', ',', ':', '=', ';', '?', '[', ']', '{', '}', '-',
    '*', '/', '+', '!', '<', '>'
]

def extractExtension(file):
    if file is None:
        return None
    
    validExtension = '.242'
    try:
        extension = os.path.splitext(file)[1]
    except:
        extension = None

    if extension == validExtension:
        return True
    else:
        return False 

def openFile(file_path):

    if extractExtension(file_path) == True:
        try:
            with open(file_path, 'r') as file:
                return file.read()
            file.close()

        except FileNotFoundError:
            print(f"File not founded.")

        except Exception as e:
            print(f"Exception ocurred: {e}")
    else:
        print(f'File not supported')

def test_string(letter):
    return letter == '"'

def test_caracter(atom):
    if atom == "'":
        return True

def test_special_caracter(atom):
    caracteres = ['(', ')', '[', ']', '{', '}']
    if atom in caracteres:
        return True

def add_to_dict(key, value):
    if key not in list_atoms:
        list_atoms[key] = []
    list_atoms[key].append(value)

def process_atom(atom, lineNumber):
    if atom:
        add_to_dict(atom, lineNumber)
        if not atom_in_table(atom):
            add_symbol_to_table(atom, None, list_atoms[atom], None, None, None)
        else:
            update_atom_lines(atom, list_atoms[atom])

def filter_comments(file_content):
    filtered_content = ""
    i = 0
    length = len(file_content)

    while i < length:
        if file_content[i:i+2] == "/*":
            i += 2
            while i < length and file_content[i:i+2] != "*/":
                i += 1
            i += 2 if i < length else 0
        elif file_content[i:i+2] == "//":
            i += 2
            while i < length and file_content[i] != "\n":
                i += 1
        else:
            filtered_content += file_content[i]
            i += 1
    return filtered_content

def test_string(letter):
    return letter == '"'

def test_caracter(atom):
    if atom == "'":
        return True

def test_special_caracter(atom):
    caracteres = ['(', ')', '[', ']', '{', '}']
    if atom in caracteres:
        return True

def alternate_scan(file_path):
    file = openFile(file_path)
    lineNumber = 0
    atom = ''
    flag_string = False
    file = filter_comments(file)
    for line in file.splitlines():
        lineNumber += 1
        skip_line = False

        for i, letter in enumerate(line):
            if skip_line:
                break
            if test_string(letter): 
                if flag_string: 
                    atom += letter
                    process_atom(atom, lineNumber)
                    atom = ''
                else:
                    if atom:
                        process_atom(atom, lineNumber)
                        atom = ''
                    atom += letter
                flag_string = not flag_string
                continue
            if flag_string:
                atom += letter
                continue
            if letter != '' and letter != '\n' and letter != '\t': 
                if test_special_caracter(letter):
                    process_atom(atom, lineNumber)
                    atom = letter
                    process_atom(atom, lineNumber)
                    atom = ''
                elif letter == ' ':
                    if atom:
                        process_atom(atom, lineNumber)
                        atom = ''
                elif letter == ',' or letter == ';':
                    if atom:
                        process_atom(atom, lineNumber)
                    atom = letter
                    process_atom(atom, lineNumber)
                    atom = ''
                else:       
                    atom += letter
        if atom:
            process_atom(atom, lineNumber)
            atom = ''
    return list_atoms

def isValidTokenForLanguage(caracter):
    if caracter in validTokens:
        return True
    else:
        return False

def generateLexicalReport(file_path):
    base_name = os.path.basename(file_path).split('.')[0]
    filename = f"./results/{base_name}_lexical_report.LEX"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"{header}\nRELATÓRIO DA TABELA DE SÍMBOLOS - {file_path}\n\n")
        for entry in LexReport:
            if (entry[0]!='header'):
                f.write(f"Lexeme: {entry[0]}, Código: {entry[1]}, ÍndiceTabSim: {entry[2]}, Linha: {entry[3]}\n{divider}")
    print(f"Relatório gerado em {filename}")

def addToLexReport(atom, code, lineNumber):
    newEntry = [
        atom,
        code,
        getIndex(atom, code),
        lineNumber
    ]
    LexReport.append(newEntry)
