import sys
import random

def myPrint(msg):
    sys.stdout.buffer.write(msg.encode())
    sys.stdout.flush()
    
def guessNumber():
    myPrint("Please enter the minimum number : ")
    minNumByte = sys.stdin.buffer.readline()
    minNum = minNumByte.decode("utf-8")

    myPrint("Please enter the maximum number : ")
    maxNumByte = sys.stdin.buffer.readline()
    maxNum = maxNumByte.decode("utf-8")

    if type(int(minNum)) != int or type(int(maxNum)) != int:
        myPrint("Please enter a number.")
        sys.exit(1)

    minNum = int(minNum)
    maxNum = int(maxNum)
    
    if minNum >= maxNum:
        myPrint("Please enter a number smaller than maximum number for minimum number.")
        sys.exit(1)

    ansNum = random.randint(minNum, maxNum)
    flag = False

    myPrint("How many times do you want to try? : ")
    tryNumByte = sys.stdin.buffer.readline()
    tryNum = tryNumByte.decode("utf-8")

    for i in range(int(tryNum)):
        myPrint("Please choose a number between minimum number and maximum number : ")
        guessByte = sys.stdin.buffer.readline()
        guessNum = guessByte.decode("utf-8")

        if type(int(guessNum)) != int:
            myPrint("Please enter a number.")
            sys.exit(1)

        guessNum = int(guessNum)

        if guessNum == ansNum:
            myPrint("Correct answer!")
            flag = True
            sys.exit(0)
        elif guessNum > ansNum:
            myPrint("Correct answer is a smaller number.\n")
        else: 
            myPrint("Correct answer is a bigger number.\n")
    
    if flag == False:
        myPrint("Please retry:)\n")

if __name__ == "__main__":
    guessNumber()