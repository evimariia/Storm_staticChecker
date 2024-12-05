from syntatic_analyzer import reservedWordsAndSymbols, identifiers
from symbol_table import add_symbol_to_table, atom_in_table, update_atom_lines
import os
import re

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

sei_la = ['$', '.', "'", '"', ' ', '%', '(', ')', ',', ';', '?', '[', ']', '{', '}', '-', '*', '/', '+', '!']

possivel_cadeia = r'^"|"[A-Za-z0-9]*"$'
possivel_caracter = r"^'|'[A-Z']'$"
possivel_num_inteiro = r'^[0-9]+$'
possivel_num_real = r'^[+-]?(\d+((,\d+)+)?|\d+(\.\d+)?|\.\d+)([eE][+-]?\d+)?$'
possivel_variavel = r'^[A-Za-z0-9]+$'

def check_type(atomo):

    if re.match(possivel_cadeia, atomo):
        return True, "C01", "cadeia"
    if re.match(possivel_caracter, atomo):
        return True, "C02", "caracter"
    if re.match(possivel_num_inteiro, atomo):
        return True, "C03", "inteiro"
    if re.match(possivel_num_real, atomo):
        return True, "C04", "real"
    if re.match(possivel_variavel, atomo):
        return True, "C07", "variavel"
    else:
        return True, "C07", "variavel"

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

def findKeyByValue(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None 

def scan(file_path):
    file = openFile(file_path)
    lineNumber = 0
    control = {'previous':None, 'actual':None, 'next': None, 'line':[]}
    list_atoms = []
    atom_aux = ''
    atom = ''

    for line in file.splitlines():
        lineNumber += 1
        for words in line.split():
            word_length = len(words)
            i = 0
            while i < word_length:
                letter = words[i]
                next_letter = words[i + 1] if i + 1 < word_length else None  

                # Verifica se a letra atual é válida
                if isValidTokenForLanguage(letter):
                    atom_aux += letter
                    atom = atom_aux
                else:
                    print("False")

            control['actual'] = atom

            if isValidTokenForPattern(str(control['actual']) + atom_aux):
                atom = str(control['actual']) + atom_aux
                list_atoms.append(atom)

            elif isValidTokenForPattern(atom):
                list_atoms.append(atom)
                control['previous'] = atom
                atom_aux = ''
                atom = ''
    
            if (atom != None) and (atom != '') and (atom != '\n') and (atom != '\t') and (atom not in reservedWordsAndSymbols.values()):
                list_atoms.append(atom) 

            if (atom != None) and (atom in list_atoms) and (atom not in reservedWordsAndSymbols.values()):
                tipo = check_type(atom)[1]
                existed = any(atom in lista for lista in identifiers.values())
                if not existed in identifiers:
                    identifiers[tipo].append(atom)
                control['previous'] = atom

            
            atom_aux = ''
            atom = ''  

    print(f'atomo: {atom}')

def test_string(atom):
    if atom == '"':
        return True

def test_caracter(atom):
    if atom == "'":
        return True

def test_short_comment(atom):
    if atom == '//':
        return True

def test_long_comment(atom):
    if atom == '/*':
        return True

def test_special_caracter(atom):
    caracteres = ['(', ')', '[', ']', '{', '}']
    if atom in caracteres:
        return True
    
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


def alternate_scan(file_path):
    file = openFile(file_path)
    if not file:
        return

    file = filter_comments(file)
    lineNumber = 0
    list_atoms = {}  
    atom = ''

    for line in file.splitlines():
        lineNumber += 1
        for words in line.split():
            for letter in words:
                if letter not in ['\n', '\t', '']:  
                    if test_special_caracter(letter):  
                        if atom:
                            process_atom(atom, lineNumber, list_atoms)
                            atom = ''
                        process_atom(letter, lineNumber, list_atoms)  
                    else:
                        atom += letter  
                else:
                    atom = ''  

            if atom:  
                process_atom(atom, lineNumber, list_atoms)
                atom = ''

    print(f"Atomos e linhas: {list_atoms}")

def process_atom(atom, lineNumber, list_atoms):
    is_valid, atom_code, atom_type = check_type(atom)  
    if not is_valid:
        print(f"Atomo inválido encontrado: {atom}")
        return
    else:
        is
    if atom not in list_atoms:
        list_atoms[atom] = [lineNumber]
    else:
        list_atoms[atom].append(lineNumber)
    if not atom_in_table(atom):
        if atom_code == "C07":
            print(atom_code)
            #atom = truncagem(atom)
        add_symbol_to_table(atom, atom_code, list_atoms[atom], atom_type, len(atom), len(atom))
    else:
        update_atom_lines(atom, lineNumber)

def truncagem(atom_string, max_length=30):
    valid_chars = ""  
    count = 0         
    is_valid = True   

    for char in atom_string:
        if count < max_length:  
            valid_chars += char
            count += 1
        else:
            if is_delimiter(char):  
                break
            
    if is_number(valid_chars) and not is_valid_number(valid_chars):
        valid_chars = fix_number(valid_chars)

    return valid_chars


def lexicalAnalyze():
    return 0

def isValidTokenForLanguage(caracter):
    if caracter in validTokens:
        return True
    else:
        return False

def isValidTokenForPattern(atom):
    for value in reservedWordsAndSymbols.values():
        if atom == value:
            atomCode = findKeyByValue(reservedWordsAndSymbols, atom)
            return True
            break
        elif isinstance(atom, str):
            pass

def generateLexicalReport():
    return None

file_path = r"C:\Users\reisb\OneDrive\Documentos\teste.242"
alternate_scan(file_path)
