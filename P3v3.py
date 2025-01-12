symbol_table = {
    'carro': '%',
    'acidente': '$',
    'senhor': '&',
    'do': '#'
}

def encode_text(text):
    encoded_text = ''
    for word in text.split():
        encoded_word = symbol_table.get(word, word)
        encoded_text += encoded_word + ' '

    return encoded_text.strip()


def calculate_compression_ratio(original_text, compressed_text):
    original_chars = len(original_text)
    compressed_chars = len(compressed_text)

    compression_ratio = compressed_chars / original_chars

    return compression_ratio


# Receber o texto de entrada
original_text = input("Digite o texto a ser comprimido: ")

# Substituir palavras pelos símbolos correspondentes
compressed_text = encode_text(original_text)
compression_ratio = calculate_compression_ratio(original_text, compressed_text)

# Exibir a saída no formato dos casos de teste
print("Entrada:")
print(original_text)
print("Saída:")
print(compressed_text)
print("Taxa de compressão: {:.2f}%".format(compression_ratio * 100))
