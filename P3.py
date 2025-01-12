dict = {'carro': '%', 'acidente': '$', 'senhor': '&', 'do': '#'} #dictionary with for keyword enconding

text = input().split() #input text

for i in range(len(text)): #starting a loop to go through the text
    if text[i] in dict: #checking if the word is on the dictionary
        text[i] = dict[text[i]] #replacing the word by the symbol

print(*text) #printing the new text
