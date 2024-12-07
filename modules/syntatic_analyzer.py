from lexical_analyzer import list_atoms
from symbol_table import update_atom_code, update_atom_type

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
    'D01': 'subMáquina'
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

possivel_cadeia = r'^"|"[A-Za-z0-9]*"$'
possivel_caracter = r"^'|'[A-Z']'$"
possivel_num_inteiro = r'^[0-9]+$'
possivel_num_real = r'^[+-]?(\d+((,\d+)+)?|\d+(\.\d+)?|\.\d+)([eE][+-]?\d+)?$'
possivel_variavel = r'^[A-Za-z0-9]+$'

def check_type(atomo):

    if re.match(possivel_cadeia, atomo):
        update_atom_type(atomo, 'consCadeia')
        identifiers['C01'].append(atomo)
        return True, "C01", "cadeia"
    
    if re.match(possivel_caracter, atomo):
        update_atom_type(atomo, 'consCaracter')
        identifiers['C02'].append(atomo)
        return True, "C02", "caracter"
    
    if re.match(possivel_num_inteiro, atomo):
        update_atom_type(atomo, 'consInteiro')
        identifiers['C03'].append(atomo)
        return True, "C03", "inteiro"
    
    if re.match(possivel_num_real, atomo):
        update_atom_type(atomo, 'consReal')
        identifiers['C04'].append(atomo)
        return True, "C04", "real"
    
    if re.match(possivel_variavel, atomo):
        update_atom_type(atomo, 'variavel')
        identifiers['C07'].append(atomo)
        return True, "C07", "variavel"
    else:
        return True, "C07", "variavel"

def findKeyByValue(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None 

def isValidTokenForPattern(atom):
    for value in reservedWordsAndSymbols.values():
        if atom == value:
            atomCode = findKeyByValue(reservedWordsAndSymbols, atom)
            return atomCode
            break
        elif isinstance(atom, str):
            pass

def classify_atoms(list_atoms):
    for atom in list_atoms.keys():
        if atom in reservedWordsAndSymbols.values():
            update_atom_code(atom, isValidTokenForPattern(atom))
        else:
            check_type(atom)
    print('fim')

classify_atoms(list_atoms)

#elementos dos relatórios
divider = "==============================================\n"
header = """Equipe 04: os caras do momento.
            Componentes:
            Bruno da Costa Sales, bruno.sales@aln.senaicimatec.edu.br, (71)99650-1212
            Évila Maria de Souza Carneiro, evila.carneiro@aln.senaicimatec.edu.br, (71)
            Gabriel Batista Reis, gabriel.b@aln.senaicimatec.edu.br, o memso de samplix
            João Victor Borges Lima, joao.l@aln.senaicimatec.edu.br, (71)4002-8922\n
            """
