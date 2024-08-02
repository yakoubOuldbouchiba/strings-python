# Caesar cipher.
text = input("Enter your message: ")
can_enter_shift_value = True;
while can_enter_shift_value :
    shift_value = int(input("Enter your shift value"))
    if(shift_value > 0 and shift_value<=26 ):
      can_enter_shift_value = False;  
cipher = ''
while shift_value !=0  :
    for char in text:
        if  char.isspace():
            cipher += " "
        if not char.isalpha():
           cipher += str(char)
        else :
            code = ord(char) + 1
            if code > ord('Z') and char.isupper():
                code = ord('A')
            if code > ord('z') and char.islower():
                code = ord('a')
            cipher += chr(code)
    text=cipher
    cipher = ''
    shift_value-=1
    
print(text)