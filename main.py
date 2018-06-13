
# Specific uses in Pig-Latin
#SOMEONE CHECK THIS FILE
def t(str):
    #Returns the 2 letters added together to check against
    return str[0]+str[1]

# Speicfic use characters                
lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
# My input section
sentence = input('Type what you would like translated into pig-latin and press ENTER: ')
# sentence.split() converts the sentence into a list per word
sentence = sentence.split()
for k in range(len(sentence)):
    i = sentence[k]
    # Checks for any NON alphabetical characters
    if i.isalpha() == False:
        # Checks for any digits in the input string
        if i[0].isdigit() == True:
            sentence[k] = i
        elif i[0] in ['a', 'e', 'i', 'o', 'u']:
            if i.find("'") or i.find("-"):
                sentence[k] = i+'ay'
            else:
                sentence[k] = i[0:-1]+'ay'+i[-1]
        elif t(i) in lst:
            if i.find("'") or i.find("-"):
                sentence[k] = i[2:]+i[:2]+'ay'
            else:
                sentence[k] = i[2:-1]+i[:2]+'ay'+i[-1]
        else:
            if i.find("'") or i.find("-"):
                sentence[k] = i[1:]+i[0]+'ay'
            else:
                sentence[k] = i[1:-1]+i[0]+'ay'+i[-1]
    #Apparently isalpha() does not account for . or ? at the end of a sentence, so I did.
    elif i[-1] == "." or i[-1] == "?":
        if i[0] in ['a', 'e', 'i', 'o', 'u']:
            sentence[k] = i[0:-1]+'ay'+i[-1]
        elif t(i) in lst:
            sentence[k] = i[2:-1]+i[:2]+'ay'+i[-1]
        else:
            sentence[k] = i[1:-1]+i[0]+'ay'+i[-1]
    #Checking for vowels
    elif i[0] in ['a', 'e', 'i', 'o', 'u']:
        sentence[k] = i+'ay'
    #Checking for the lst up top (All of the combined character sounds starting a word)
    elif t(i) in lst:
        sentence[k] = i[2:]+i[:2]+'ay'
    # ANYTHING ELSE!
    else:
        sentence[k] = i[1:]+i[0]+'ay'
#Let's print this thing    
new_string = ' '.join(sentence)
print(new_string.capitalize())
