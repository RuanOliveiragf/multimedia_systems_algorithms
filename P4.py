import re

substituicoes = {
    '%': 'carro',
    '$': 'acidente',
    '&': 'senhor',
    '#': 'do'
}

def substituir_simbolos(text):
    def replace(match):
        simbolo = match.group(0)
        return substituicoes.get(simbolo, simbolo)
    
    padrao = re.compile(r'%|\$|&|#')

    return padrao.sub(replace, text)

texto = input()

texto_substituido = substituir_simbolos(texto)
print(texto_substituido)
