import os

import lexical_analyzer
import symbol_table

global atoms

file1 = r'C:\Users\evila\OneDrive\Documentos\teste1.242'
file2 = r'C:\Users\evila\OneDrive\Documentos\Anexo II - PIBIT - Évila Carneiro - Documentos Google.pdf'

# Defines the language's atoms list
atoms = {
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
    'C01': 'consCadeia',
    'C02': 'consCaracter',
    'C03': 'consInteiro',
    'C04': 'consReal',
    'C05': 'nomFuncao',
    'C06': 'nomPrograma',
    'C07': 'variavel',
    'D01': 'subMáquina1',
    'D02': 'subMáquina2',
    'D03': 'subMáquina3'
    # Add others subMáquinas here if it's necessary
}

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
        print(f'Extension not supported: {extension}')
        return False 

def openFile():
    return None

def createSyntaticTree():
    return None

print(extractExtension(file1))
print(extractExtension(file2))