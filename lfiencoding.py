#/usr/bin/python3

import hashlib as hash
import base64

import myencodings

def welcome():

    print("Please choose from the following options on what encoding you want?\n")
    
    #List creation
    mylist = ["base64", "urlencoding", "hex", "nullbyte", "All of the above"]
    
    print("1.\t", mylist[0],"\n", "2.", mylist[1], "\n", "3.\t", mylist[2])

    choice = input("")

    if choice == mylist[0]:
        #Calls the base64 function
        myencodings.basesixty()

    elif choice == mylist[1]:
        #call the url encoding function
        print("Payload is: ")
        myencodings.urlencoding()
    elif choice == mylist[2]:
        
        myencodings.hex()
    else:
        exit()    
welcome()

