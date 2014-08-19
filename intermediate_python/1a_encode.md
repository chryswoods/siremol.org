#Containers: Answer to exercise 1a

```python
letter_to_morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
                   'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
                   'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                   'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
                   '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                   '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                   ' ':'/' }

message = "SOS We have hit an iceberg and need help quickly"

morse = []

for letter in message:
    letter = letter.lower()
    morse.append(letter_to_morse[letter])

# We need to join together Morse code letters with spaces
print( " ".join(morse) )
```

# [Previous](dictionaries.md) [Up](README.md) [Next](dictionaries.md)

