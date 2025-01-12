#o codigo do odio
import re

dict = {
    'carro': '%',
    'acidente': '$',
    'senhor': '&',
    'do': '#'
}

text = input()

ori_size = len(text.encode('utf-8'))

padrao = re.compile(r'\b(carro|acidente|senhor|do)\b')
new_text = padrao.sub(lambda match: dict.get(match.group(0), match.group(0)), text)

new_size = len(new_text.encode('utf-8'))

com_rate = int((new_size / ori_size) * 100) / 100

print(new_text)
print("Taxa de compressao:{}%".format(com_rate))
