# Specific uses in Pig-Latin
def add_special_letters(str):
    # Returns the 2 letters added together to check against
    return str[0] + str[1]

def parse_sentence(sentence):
    special_letters = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl',
                       'gr', 'st', 'sl', 'cl', 'pl', 'fl']

    vowels = ['a', 'e', 'i', 'o', 'u']
    suffix = 'ay'

    new_sentence = []
    for i in sentence.split():
        # Checks for any NON alphabetical characters
        new_word = ""
        if i.isalpha():
            if i[0] in vowels:
                new_word = i + suffix
            # Checking for the special_letters up top (All of the combined character sounds starting a word)
            elif add_special_letters(i) in special_letters:
                new_word = i[2:]+i[:2] + suffix
            # ANYTHING ELSE!
            else:
                new_word = i[1:]+i[0] + suffix

        else:
            # Checks for any digits in the input string
            if i[0].isdigit():
                new_word = i
            # Checks for . ? or ! because damn
            elif i[-1] == "." or i[-1] == "?" or i[-1] == "!":
                if i[0] in vowels:
                    new_word = i[0:-1] + suffix + i[-1]
                elif add_special_letters(i) in special_letters:
                    new_word = i[2:-1]+i[:2] + suffix + i[-1]
                else:
                    new_word = i[1:-1]+i[0] + suffix + i[-1]
            # Check for vowel start
            elif i[0] in vowels:
                if i.find("'") or i.find("-"):
                    new_word = i+suffix
                else:
                    new_word = i[0:-1]+suffix+i[-1]
            # Check for special characters
            elif add_special_letters(i) in special_letters:
                if i.find("'") or i.find("-"):
                    new_word = i[2:]+i[:2]+suffix
                else:
                    new_word = i[2:-1]+i[:2]+suffix+i[-1]
            # Yeah, everything else
            else:
                if i.find("'") or i.find("-"):
                    new_word = i[1:]+i[0]+suffix
                else:
                    new_word = i[1:-1]+i[0]+suffix+i[-1]
        new_sentence.append(new_word)
    return ' '.join(new_sentence)

# My input section
sentence = input('Type what you would like translated into pig-latin and press ENTER: ')
# sentence.split() converts the sentence into a list per word

# Let's print this thing
new_sentence = parse_sentence(sentence.lower())
print("Original Sentence: " + sentence.capitalize())
print("Pig Latin-ified: " + new_sentence.capitalize())