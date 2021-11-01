while True:
    print('Press 1 to encode')
    print('Press 2 to decode')
    press = int(input("")) #input number for decode and encode
    if press == 1:       # if press 1 it will go to encode
        word1 = input("Enter the string to encode: ") #input string u want to encode
        deword = ''     # the word that u encode
        for word1 in word1:         # for word1 in if in word1 in input
            word1 = ord(word1)       #change word to ascii
            if word1 >= 65 and word1 <= 77 or word1 >= 97 and word1 <= 109:      # number of ascii value
                word1 += 13  # because it has 13 words
                word1 = chr(word1) # change acsii to letter
                deword += word1   #when the letter encode it will go to the next letter
            elif word1 >= 78 and word1 <= 90 or word1 >= 110 and word1 <= 122: #number of ascii value
                word1 -= 13  
                word1 = chr(word1)
                deword += word1
        print(f'The decoded text is: {deword}') #print the decoded result
    else:
        word1 = input("Enter the string to decode: ") # the same as the top it since it the same and just encode and decode
        deword = ''
        for word1 in word1:
            word1 = ord(word1)
            if word1 >= 65 and word1 <= 77 or word1 >= 97 and word1 <= 109:
                word1 += 13
                word1 = chr(word1)
                deword += word1
            elif word1 >= 78 and word1 <= 90 or word1 >= 110 and word1 <= 122:
                word1 -= 13
                word1 = chr(word1)
                deword += word1
        print(f'The decoded text is: {deword}')
    print("Do you want to continue?[Y/N]")
    next = input("")
    if next == "N": 
        break