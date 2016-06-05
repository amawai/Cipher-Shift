#! python3
import string

def SecretMessage():
    phrase = input("Input phrase >> ")
    user_shift_value = input("Shift value >> ")
    shift_value = 0
    correctInput = False
    while (correctInput != True):   #Ensuring the user input for shift_value is actually a number
        try:
            shift_value = int (user_shift_value) 
            correctInput = True #This is executed if the user's shift value input is valid
        except ValueError:
            user_shift_value = input("Invalid shift value! Enter a number >> ")
    
    shift_value = abs(shift_value%26) #Shift value cannot be negative or bigger than 26
    encoded_phrase = ""
    for c in phrase:
        x = ord(c) + shift_value
        if c in string.ascii_uppercase: #code numbers 65-90 for uppercase 
            if x > 90:
                x = x % 91
                if x < 65:
                    x += 65 #To return to range[65,90] since modulo yields range[0,90]
            encoded_phrase += chr(x) #use chr(x) to convert to ascii
        elif c in string.ascii_lowercase: #code number 97-122 for lowercase
            if x > 122:
                x = x % 123
                if x < 97:
                    x += 97 #To return to range[97,122] since modulo yields range[0,122]  
            encoded_phrase += chr(x) 
        else:
            encoded_phrase += c #if c is not a letter, e.g. space, punctuation, etc.
    print (encoded_phrase)

done = False
while(done != True):
    SecretMessage()
    phrase = input("Do you want to make another \"secret\" message? (y/n) >> ")
    done = True if phrase.lower()=='n' else False
    

    
