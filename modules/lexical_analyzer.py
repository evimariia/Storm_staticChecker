#import modules.syntatic_analyzer
import os
import re

global reservedWordsAndSymbols
global identifiers

# Defines the language's atoms list
reservedWordsAndSymbols = {
    'cód': 'Átomo',
    'A01': 'cadeia',
    'A02': 'caracter',
    'A03': 'declaracoes',
    'A04': 'enquanto',
    'A05': 'false',
    'A06': 'fimDeclaracoes',
    'A07': 'fimEnquanto',
    'A08': 'fimFunc',
    'A09': 'fimFuncoes',
    'A10': 'fimPrograma',
    'A11': 'fimSe',
    'A12': 'funcoes',
    'A13': 'imprime',
    'A14': 'inteiro',
    'A15': 'logico',
    'A16': 'pausa',
    'A17': 'programa',
    'A18': 'real',
    'A19': 'retorna',
    'A20': 'se',
    'A21': 'senao',
    'A22': 'tipoFunc',
    'A23': 'tipoParam',
    'A24': 'tipoVar',
    'A25': 'true',
    'A26': 'vazio',
    'B01': '%',
    'B02': '(',
    'B03': ')',
    'B04': ',',
    'B05': ':',
    'B06': ':=',
    'B07': ';',
    'B08': '?',
    'B09': '[',
    'B10': ']',
    'B11': '{',
    'B12': '}',
    'B13': '-',
    'B14': '*',
    'B15': '/',
    'B16': '+',
    'B17': '!=',
    'B18': '<',
    'B19': '<=',
    'B20': '==',
    'B21': '>',
    'B22': '>=',
    'D01': 'subMáquina1',
    'D02': 'subMáquina2',
    'D03': 'subMáquina3'
    # Add others subMáquinas here if it's necessary
}

#consCadeia começa e termina com aspas duplas
#consCaracter começa e termina com aspas simples
identifiers = {
    'C01': ['consCadeia'],
    'C02': ['consCaracter'],
    'C03': ['consInteiro'],
    'C04': ['consReal'],
    'C05': ['nomFuncao'],
    'C06': ['nomPrograma'],
    'C07': ['variavel']
}

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

def check_type(atomo):
    possivel_cadeia = r'^"|"[A-Za-z0-9]*"$'
    possivel_caracter = r"^'|'[A-Z']'$"
    possivel_num_inteiro = r'^[0-9]+$'
    possivel_num_real = r'^[+-]?(\d+((,\d+)+)?|\d+(\.\d+)?|\.\d+)([eE][+-]?\d+)?$'
    possivel_variavel = r'^[A-Za-z0-9]+$'

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

                    '''if letter == ' ' or letter == '\n':
                        list_atoms.append(atom)
                        atom_aux = ''
                        atom = ''
                        break'''

            control['actual'] = atom

            if isValidTokenForPattern(str(control['actual']) + atom_aux):
                atom = str(control['actual']) + atom_aux
                list_atoms.append(atom)

            elif isValidTokenForPattern(atom):
                list_atoms.append(atom)
                control['previous'] = atom
                atom_aux = ''
                atom = ''
    
            if atom != None and atom != '' and atom != '\n' and atom != '\t':
                list_atoms.append(atom) 

            if (atom != None) and (atom in list_atoms) and (atom not in reservedWordsAndSymbols.values()):
                print(type(atom))
                tipo = check_type(atom)[1]
                existed = any(atom in lista for lista in identifiers.values())
                if not existed in identifiers:
                    identifiers[tipo].append(atom)
                control['previous'] = atom

            
            atom_aux = ''
            atom = ''  

        print(f'atomo: {atom}')
    print('cabou')

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
            print(value)
            atomCode = findKeyByValue(reservedWordsAndSymbols, atom)
            return True
            break
        elif isinstance(atom, str):
            pass

def generateLexicalReport():
    return None

file_path = r"C:\Users\evila\OneDrive\Documentos\teste1.242"
scan(file_path)