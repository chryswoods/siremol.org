class Morse:
    def __init__(self):
        self._letter_to_morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.',
                   'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--',
                   'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                   'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
                   '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                   '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                   ' ':'/' }
        
        self._morse_to_letter = {}
        for letter in self._letter_to_morse.keys():
            self._morse_to_letter[ self._letter_to_morse[letter] ] = letter
        
    def encode(self, message):
        morse = []
        for letter in message:
            morse.append( self._letter_to_morse[letter.lower()] )
        return morse
    
    def decode(self, morse):
        message = []
        for code in morse:
            message.append( self._morse_to_letter[code] )
        return "".join(message)

if __name__ == "__main__":
    morse = Morse()

    for message in ["Hello world", "something to encode", "test message"]:
        test = morse.decode( morse.encode(message) )

        if message.lower() == test:
            print("Success: %s" % message)
        else:
            print("Failed: %s" % message)
