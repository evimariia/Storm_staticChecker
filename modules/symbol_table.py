import modules.lexical_analyzer
import numpy

global symbolTable

# Create a empty symbol table for each source text analyzed
#symbolTable = [
#    ['atom', 'code', 'line', 'type'],
#    []
#]

def createSymbolTable():
    symbolTable = numpy.array(['Entry', 'lexeme', 'code', 'type', 'line'])
    return None

def searchSymbol(code):

    return 0

def addSymbol(atom,code, type, line):
    if searchSymbol(code) == 0:
        entry =+ 1
        newEntry = numpy.array([entry, atom, code, type, line])
        symbolTable = numpy.vstack(symbolTable, newEntry)
    return 0 

def generateTableReport():
    report = open()
    return None