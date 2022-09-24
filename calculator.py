import re

# This is a form of calculator where u can type the math quistion, 
# and using Regex the program will give you the answer

amountOfDivisions=0
amountOfMultiplications=0
amountOfAddition=0
amountOfASubtration=0

print("start by giving me a math expresion to solve. You can use [+] [-] [/] [*] [()]:")
print("eg. you say: (4/(5*6))*(5/9)+5*(5-6) and i'll answer: -4.925925925925926")
StartMathExpresion = input(":")
currentMathExpresion = StartMathExpresion.replace(" ", "")

amountOfStartParentheses = len((re.findall(r'[\(]',StartMathExpresion)))
amountOfEndParentheses = len((re.findall(r'[\)]',StartMathExpresion)))

if (amountOfStartParentheses != amountOfEndParentheses):
    print("parantheses error in", currentMathExpresion)
    exit()

def Calculate(currentMathExpresion):
    amountOfDivisions=len((re.findall(r'(\w)[/]',currentMathExpresion)))
    amountOfMultiplications=len((re.findall(r'(\w)[*]',currentMathExpresion)))
    amountOfAddition=len((re.findall(r'(\w)[+]',currentMathExpresion)))
    amountOfASubtration=len((re.findall(r'(\w)[-]',currentMathExpresion)))


    def divide (currentMathExpresionL):
        PlusMinus = False
        word1=(re.search(r'(\d*\.?\d*)[/]',currentMathExpresionL))
        word2=(re.search(r'[/](\d*\.?\d*)',currentMathExpresionL))
        if (int(len(word2.group(1)) < 1)):
            word2=(re.search(r'[/]([\-?]\d*\.?\d*)',currentMathExpresionL))
            PlusMinus = True

        tempResult = float(word1.group(1)) / float(word2.group(1))
        if(PlusMinus == False):
            currentMathExpresionL = currentMathExpresionL.replace(re.search(r'(\d*\.?\d*[/]\d*\.?\d*)',currentMathExpresionL).group(1), str(tempResult))
        else:
            currentMathExpresionL = currentMathExpresionL.replace(re.search(r'(\d*\.?\d*[/][\-?]\d*\.?\d*)',currentMathExpresionL).group(1), str(tempResult))
        return currentMathExpresionL

    def Multiply (currentMathExpresionL):
        PlusMinus = False
        word1=(re.search(r'(\d*\.?\d*)[*]',currentMathExpresionL))
        word2=(re.search(r'[*](\d*\.?\d*)',currentMathExpresionL))
        if (int(len(word2.group(1)) < 1)):
            word2=(re.search(r'[*]([\-?]\d*\.?\d*)',currentMathExpresionL))
            PlusMinus = True

        tempResult = float(word1.group(1)) * float(word2.group(1))
        if(PlusMinus == False):
            currentMathExpresionL = currentMathExpresionL.replace(re.search(r'(\d*\.?\d*[*]\d*\.?\d*)',currentMathExpresionL).group(1), str(tempResult))
        else:
            currentMathExpresionL = currentMathExpresionL.replace(re.search(r'(\d*\.?\d*[*][\-?]\d*\.?\d*)',currentMathExpresionL).group(1), str(tempResult))
        return currentMathExpresionL

    #Driver for multiplication and division
    DriveTimes = amountOfDivisions + amountOfMultiplications
    for i in range(DriveTimes):
        Symbol = (re.search(r'([/|*])',currentMathExpresion))
        if (Symbol.group(1) == "/"):
            currentMathExpresion = divide(currentMathExpresion)
        elif(Symbol.group(1) == "*"):
            currentMathExpresion = Multiply(currentMathExpresion)



    for AdditionsNumber in range(amountOfAddition):
        PlusMinus = False
        word1=(re.search(r'(\d*\.?\d*)[+]',currentMathExpresion))
        word2=(re.search(r'[+](\d*\.?\d*)',currentMathExpresion))
        if (int(len(word2.group(1)) < 1)):
            word2=(re.search(r'[+]([\-?]\d*\.?\d*)',currentMathExpresion))
            PlusMinus = True

        tempResult = float(word1.group(1)) + float(word2.group(1))
        if(PlusMinus == False):
            currentMathExpresion = currentMathExpresion.replace(re.search(r'(\d*\.?\d*[+]\d*\.?\d*)',currentMathExpresion).group(1), str(tempResult))
        else:
            currentMathExpresion = currentMathExpresion.replace(re.search(r'(\d*\.?\d*[+][\-?]\d*\.?\d*)',currentMathExpresion).group(1), str(tempResult))

    for SubtractionsNumber in range(amountOfASubtration):
        PlusMinus = False
        word1=(re.search(r'(\d*\.?\d*)[-]',currentMathExpresion))
        word2=(re.search(r'[-](\d*\.?\d*)',currentMathExpresion))
        if (int(len(word2.group(1)) < 1)):
            word2=(re.search(r'[-]([\-?]\d*\.?\d*)',currentMathExpresion))
            PlusMinus = True

        tempResult = float(word1.group(1)) - float(word2.group(1))
        if(PlusMinus == False):
            currentMathExpresion = currentMathExpresion.replace(re.search(r'(\d*\.?\d*[-]\d*\.?\d*)',currentMathExpresion).group(1), str(tempResult))
        else:
            currentMathExpresion = currentMathExpresion.replace(re.search(r'(\d*\.?\d*[-][\-?]\d*\.?\d*)',currentMathExpresion).group(1), str(tempResult))


    return currentMathExpresion

def CheckParantheses(Expresion):
    inner = Expresion
    if (len((re.findall(r'[\(]',Expresion))) > 1):
        inner = (re.search(r'[\(].*?([\(].*?[\)])',Expresion).group(1))
        CheckParantheses(inner)
    else:
        CalculateParantheses(inner)
    

def CalculateParantheses(Expresion):
    resultOfParanthese = Calculate(Expresion)
    resultOfParanthese = str(resultOfParanthese).replace('(', '')
    resultOfParanthese = str(resultOfParanthese).replace(')', '')
    global currentMathExpresion
    currentMathExpresion = currentMathExpresion.replace(Expresion, str(resultOfParanthese))


for i in range(amountOfStartParentheses):
    CheckParantheses((re.search(r'([\(].*?[\)])',currentMathExpresion).group(1)))

currentMathExpresion =  Calculate(currentMathExpresion)


print(StartMathExpresion, "=", currentMathExpresion)