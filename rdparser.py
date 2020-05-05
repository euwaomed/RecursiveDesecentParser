ip = -1
userInput = ""
nextSymbol = ""
e_Value = 0
d_Value = 0
succeeded = True


# Keeps all variables declared globally as they are.
# N_value is not included as the globally declared variables
def globalVariables():
    global userInput, nextSymbol, e_Value, d_Value, succeeded, ip
    ip = -1
    userInput = ""
    nextSymbol = ""
    e_Value = 0
    d_Value = 0
    succeeded = True


# No longer used this function since we need to use a test file
# def getInputLine():
# global userInput =
# input("Enter your string. Input a \'$\' at end for it work: ")


# The allows us get the next symbol in the string or array
def getNextSymbol():
    global ip, userInput
    ip += 1
    return userInput[ip]


# End of Line statement
# We use the symbol known as $ to verify the EOL. If it isn't there,
# it will output failure even if it does the calculations.
def EOL():
    global ip, userInput
    if userInput[ip] == "$":
        return True
    else:
        return False


# The function for the Recursive Descent Parser (RDP)
# lineInput is a parameter to be used as a way use the
# expressions in the test file as strings in this assignment
def rdParser(lineInput):
    global succeeded, userInput, ip, nextSymbol
    # while not EOF:
    # getInputLine()
    userInput = lineInput
    succeeded = True
    nextSymbol = getNextSymbol()
    eList()
    if succeeded:
        print("Success")
    else:
        print("")
        print("Failure")
    globalVariables()


# This is Elist()
def eList():
    global succeeded
    E()
    if succeeded:
        eList_Tail()


# This is EList'()
def eList_Tail():
    global nextSymbol, e_Value, succeeded, ip, userInput
    if EOL():
        print(e_Value)
    else:
        if userInput[ip] == ",":
            print(e_Value, end=" ")
            nextSymbol = getNextSymbol()
            eList()
        else:
            succeeded = False


# This is E()
# N-Value is declared locally in this function
def E():
    n_Value = 0
    n_Value_ref = [n_Value]  # This was the way to ensure that the N_Value passes by reference for N() and N'()
    n_Value = N(n_Value_ref)[0]
    if succeeded:
        eTail(n_Value)


# This is E'()
# N-Value is a pass-by-value parameter in this function
def eTail(n_Value):
    global nextSymbol, e_Value, succeeded, ip, userInput
    if not (nextSymbol == "," or EOL()):
        if nextSymbol == "^":
            nextSymbol = getNextSymbol()
            E()
            e_Value = n_Value ** e_Value
        else:
            succeeded = False
    elif n_Value is not None:
        e_Value = n_Value


# This is N()
# N-Value is a pass-by-reference parameter in this function
def N(n_Value_ref):
    global succeeded, d_Value
    D()
    if succeeded:
        n_Value_ref[0] = (n_Value_ref[0] * 10) + d_Value
        nTail(n_Value_ref)
        return n_Value_ref


# This is N'()
# N-Value is also a pass-by-reference parameter in this function
def nTail(n_Value_ref):
    global nextSymbol
    if not ((nextSymbol == '^' or nextSymbol == ",") or EOL()):
        N(n_Value_ref)


# This is D()
def D():
    global d_Value, nextSymbol, succeeded, ip, userInput
    if nextSymbol.isdigit():
        d_Value = int(nextSymbol)
        # if not EOL():
        nextSymbol = getNextSymbol()
    else:
        succeeded = False


# EOF
# This functions reads the test file and executes the rdParser() function line by line.
file = open("test", "r")
for line in file:
    print(line)
    rdParser(line)
    print("-------------------")
    print("-------------------")
    print("-------------------")
