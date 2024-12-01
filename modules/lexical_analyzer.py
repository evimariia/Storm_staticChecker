#import modules.syntatic_analyzer
import os
import argparse

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

delimitador = {' ', '\n', '\t', ';', '(', ')', '{', '}', ',', '+', '-', '*', '/', '=', '<', '>', '!', '&', '|'}
   

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

                # Verifica se o próximo caractere é válido
                if next_letter and isValidTokenForLanguage(next_letter):
                    atom_seguinte = atom + next_letter
                else:
                    atom_seguinte = None  # Reseta se o próximo caractere não for válido

                # Verifica se a sequência atual forma um átomo válido
                if atom_seguinte and isValidTokenForPattern(atom_seguinte):
                    print(f'Proximo: Atomo valido identificado: {atom_seguinte}')
                    atom_aux = ''
                    atom = ''  
                    atom_seguinte = ''
                    i += 1  # Avança o índice manualmente para pular para o próximo caractere
                elif isValidTokenForPattern(atom):
                    print(f'Atual: Atomo valido identificado: {atom}')
                    atom_aux = ''
                    atom = '' 
                
                i += 1  # Avança o índice para a próxima letra

    print(file.splitlines())


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
            return atomCode
            break
        elif isinstance(atom, str):
            pass

def generateLexicalReport():
    return None

file_path = r"C:\Users\reisb\OneDrive\Documentos\teste.242"
scan(file_path)