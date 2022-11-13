code_user = input("")

#print command line
if code_user == "!print":
    code_user = input("What shall i print? ")
    input(code_user + " [press enter to continue also close and reopen the language if you are entering another command] ")
    
    code_user = input("")   

#add numbers
elif code_user == "!plus":
    num1 = input("what is the first num i shall add? ")
    num2 = input("what is the second num i shall add? ")
    print(float(num1) + float(num2))
    input("[press enter to continue also close and reopen the language if you are entering another command]")
    code_user = input("")


#subtract numbers
elif code_user == "!minus":
    num1 = input("what is the first num i shall subtract? ")
    num2 = input("what is the second num i shall subtract? ")
    print(float(num1) - float(num2))
    input("[press enter to continue]")
    code_user = input("")


#times numbers
elif code_user == "!times":
    num1 = input("what is the first num i shall times? ")
    num2 = input("what is the second num i shall times? ")
    print(float(num1) * float(num2))
    input("[press enter to continue also close and reopen the language if you are entering another command]")
    code_user = input("")


#divide numbers
elif code_user == "!divide":
    num1 = input("what is the first num i shall divide? ")
    num2 = input("what is the second num i shall divide? ")
    print(float(num1) / float(num2))
    input("[press enter to continue also close and reopen the language if you are entering another command]")
    code_user = input("")

#say the creator
elif code_user == "!creator":
    print("This coding launguage is made by RamPlayzTheEpic also Known as Ram Buddharaju!")
    input("[press enter to continue also close and reopen the language if you are entering another command]")


#see the version
elif code_user == "!version":
    input("The current version you are useing for x of death is 1.0.1 [press enter to continue also close and reopen the language if you are entering another command]")
    code_user = input("")


#repeater

elif code_user == "!repeater":
    while True:
        repeat_text = input("repeated text: ")
        input(repeat_text + " [press enter to continue also close and reopen the language if you are entering another command]")

    code_user = input("")

#