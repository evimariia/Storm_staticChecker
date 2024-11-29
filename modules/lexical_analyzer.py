import re
import os
import modules.symbol_table as symTable

global reservedWordsAndSymbols
global identifiers

# Define a lista de átomos da linguagem
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

# Identificadores (ex.: constantes e variáveis)
identifiers = {
    'C01': ['consCadeia'],
    'C02': ['consCaracter'],
    'C03': ['consInteiro'],
    'C04': ['consReal'],
    'C05': ['nomFuncao'],
    'C06': ['nomPrograma'],
    'C07': ['variavel']
}

# Tokens válidos para a linguagem
validTokens =  [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
    '_', '$', '.', "'", '"', ' '
]

# Funções para validar diferentes tipos de tokens, como strings, caracteres, números, variáveis
possivel_cadeia = r'^"|"[A-Za-z0-9]*"$'
possivel_caracter = r"^'|'[A-Z']'$"
possivel_num_inteiro = r'^[0-9]+$'
possivel_num_real = r'^[+-]?(\d+((,\d+)+)?|\d+(\.\d+)?|\.\d+)([eE][+-]?\d+)?$'
possivel_variavel = r'^[A-Za-z0-9]+$'

# Caracteres que devem ser ignorados
caracteres_invalidos = ['@']

# Função para verificar se a extensão do arquivo é válida
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

# Função para abrir o arquivo
def openFile(file_path):
    if extractExtension(file_path) == True:
        try:
            with open(file_path, 'r') as file:
                return file.read()

        except FileNotFoundError:
            print(f"File not found.")

        except Exception as e:
            print(f"Exception occurred: {e}")
    else:
        print(f'File not supported')

# Função que valida e forma os átomos
def atomo_valido(atomo):
    atomo_lower = atomo.lower()  # Ignora o case

    # Verifica se o átomo é uma palavra reservada ou símbolo
    if atomo_lower in map(str.lower, reservedWordsAndSymbols.values()):
        for key, value in reservedWordsAndSymbols.items():
            if value.lower() == atomo_lower:
                return True, key, "reservedWordOrSymbol"
    
    # Verifica se o átomo é um identificador válido
    for key, values in identifiers.items():
        if atomo_lower in map(str.lower, values):
            return True, key, "identifier"

    # Checa padrões com expressões regulares
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
    
    return False, "", ""

# Função que realiza a análise léxica, formando os átomos
def scan(file_path):
    file = openFile(file_path)    
    lineNumber = 0
    atom = ''
    
    for line in file.splitlines():
        lineNumber += 1
        print('==================================================')
        print(f'Line{lineNumber}: {line}')
        for words in line.split():
            print(f'Words: {words}')
            for letter in list(words):
                if isValidTokenForLanguage(letter):
                    atom += letter  # Constrói o possível átomo
                else:
                    # Tenta validar o átomo formado até o momento
                    atomo_valido_flag, codigo, tipo = atomo_valido(atom)
                    if atomo_valido_flag:
                        print(f"Átomo válido: {atom} | Código: {codigo} | Tipo: {tipo}")
                        atom = ''  # Reseta o átomo para formar um novo
                    else:
                        print(f"Átomo inválido: {atom}")
                        atom = letter  # Continua a partir do token atual
                        
            # Ao fim da palavra, valida o átomo se algo foi acumulado
            if atom:
                atomo_valido_flag, codigo, tipo = atomo_valido(atom)
                if atomo_valido_flag:
                    #symTable.addSymbol(atom, codigo, tipo,lineNumber)
                    print(f"Átomo válido (fim de palavra): {atom} | Código: {codigo} | Tipo: {tipo}")
                atom = ''  # Reseta o átomo

# Função que verifica se o caractere é válido na linguagem
def isValidTokenForLanguage(caracter):
    return caracter in validTokens

# Função principal para análise léxica
def lexicalAnalyze():
    return 0

# Função para gerar um relatório léxico (caso necessário no futuro)
def generateLexicalReport():
    return None