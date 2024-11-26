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

validTokens =  [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
    '_', '$', '.', "'", '"', ' '
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

        except FileNotFoundError:
            print(f"File not founded.")

        except Exception as e:
            print(f"Exception ocurred: {e}")
    else:
        print(f'File not supported')

def scan(file_path):
    file = openFile(file_path)    
    lineNumber = 0
    control = {'previous':None, 'actual':None, 'next': None, 'line':lineNumber}
    atom = ''
    
    for line in file.splitlines():
        lineNumber += 1
        print(f'Line: {line}')
        for words in line.split():
            print(f'Words: {words}')
            for letter in list(words):
                if isValidTokenForLanguage(letter):
                    print('True')
                    atom += letter
                    print(f'atomo: {atom}')

    print(file.splitlines())

def lexicalAnalyze():
    return 0

def isValidTokenForLanguage(caracter):
    if caracter in validTokens:
        return True
    else:
        return False

def isValidTokenForPattern():
    return False

def generateLexicalReport():
    return None