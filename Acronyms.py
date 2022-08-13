user_input = str(input("Ener a Phrase: "))
text = user_input.split()
Acronyms = " "
for i in text:
    Acronyms = Acronyms+str(i[0]).upper()
print(Acronyms)