from syntatic_analyzer import reservedWordsAndSymbols, identifiers
from symbol_table import add_symbol_to_table, atom_in_table, update_atom_lines
import os
import re

global list_atoms
list_atoms = {'atom':'lines'}

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
            for letter in list(words):
                if isValidTokenForLanguage(letter):
                    atom_aux += letter
                    atom = atom_aux

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

def test_string(letter):
    return letter == '"'

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

def alternate_scan(file_path):
    file = openFile(file_path)
    lineNumber = 0
    atom = ''
    flag_string = False
    
    for line in file.splitlines():
        lineNumber += 1
        skip_line = False

        for i, letter in enumerate(line):
            if skip_line:
                break

            if test_string(letter): # Verifies if the letter is the start or the end of a string by detecting " caracter

                if flag_string: # If it's inside a string it keeps constructing the atom until another " is detected
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
                if test_short_comment(atom):
                    atom += line[i:]  
                    skip_line = True
                    break 

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

    print(f'atomo: {list_atoms.keys()}')


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

file_path = r"C:\Users\evila\OneDrive\Documentos\teste1.242"
alternate_scan(file_path)