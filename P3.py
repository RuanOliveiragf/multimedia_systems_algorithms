dict = {'carro': '%', 'acidente': '$', 'senhor': '&', 'do': '#'} #dictionary with keyword encoding

text = input() #input text

ori_size = len(text) #saving the original text size

text = text.split() #separating the text into words

for i in range(len(text)): #starting a loop to go through the text
    if text[i] in dict: #checking if the word is in the dictionary
        text[i] = dict[text[i]] #replacing the word with the symbol

text = ' '.join(text) #turning the text into a string again

new_size = len(text) #saving the new text size

com_rate = new_size/ori_size #calculating the compression rate as a percentage

print(text)
print('Taxa de compressão:{:.2f}%'.format(com_rate)) #printing the new text with the compression rate)
