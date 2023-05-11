from random import choice
"""
Rearranged code and added a Replay feature
"""

#Topics
Names=["SAM","JOHN","HARRY"]
Gender=["BOY","GIRL","MALE","FEMALE"]
Colour=["RED","BLUE","GREEN","YELLOW"]
Sizes=["SMALL","MEDIUM","LARGE"]
Clothes=["PANTS","SHIRT","SOCKS"]
Currency=["YEN","RUPIAH","DOLLAR","DONG","POUND"]

"""Putting keys to the Topics
this will help with choosing a random topic
and allow us to print the topic name"""
All_Topics=["Names","Gender","Colour","Sizes","Clothes","Currency"]
All_Topics_Dict={
    "Names":Names,"Gender":Gender,"Colour":Colour,
    "Sizes":Sizes,"Clothes":Clothes,"Currency":Currency
}

#Possible actions made by user
def Correct_Guess(P1):  #P1 refers to the user input later on
    index=0
    GC=0
    for i in Word:
        if P1!=i:
            index+=1
        else:
            Display[index]=i
            index+=1
    index=0
    for Each_Letter in Display:
        if Each_Letter==Word[index]:
            GC+=1
            index+=1
        else:
            index+=1
    Unused_Letters.remove(P1)
    return GC

def Already_Guess():
    print("Letter already guessed.")

def Invalid_Guess():
    print("Please guess a letter.")

def Incorrect_Guess(P1,LL): #LL is the remaining lives left
    for i in Unused_Letters:
        if P1==i:
            Unused_Letters.remove(i)
    LL-=1
    print("Wrong guess.")
    return LL

while True:
    #Choosing Topics and Words
    Topic=choice(All_Topics)
    for Each_Key in All_Topics_Dict.keys():
        if Topic==Each_Key:
            print("Topic:",Topic)
            Topic=All_Topics_Dict[Each_Key]
            Word=choice(Topic)
            #print(Word) Uncomment if testing the randomizer
            print("Word is "+str(len(Word))+" letters long.")

    #Display is to show the players what they've guessed or not guessed per turn
    Display=[]
    for i in Word:
        Display.append("_")
    print(Display)

    #Some variables we will need
    Lives_Left=10
    Guessed_Currently=0 #This will be the amt of letters guessed right in the word
    Unused_Letters=[]
    Valid_Letters=[] #To ensure the player guesses a letter instead of special character
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        Unused_Letters.append(i)
        Valid_Letters.append(i)
        
    while Lives_Left!=0 and Guessed_Currently!=len(Word):
        P1=input("Guess here: ")
        P1=P1.upper()
        if P1 in Word and P1 in Unused_Letters:
            Guessed_Currently=Correct_Guess(P1)

        elif P1 not in Valid_Letters:
            Invalid_Guess()

        elif P1 in Valid_Letters and P1 not in Unused_Letters:
            Already_Guess()

        elif P1 in Unused_Letters and P1 not in Word:
            Lives_Left=Incorrect_Guess(P1,Lives_Left)

        print()
        print(Lives_Left,"Lives Left")
        print(Guessed_Currently,"/",len(Word),"Letters Guessed")
        print(Display)

    print()  
    if Lives_Left==0:
        print("Word was",Word,".")
        print("Better luck next time!")
    else:
        print("You got it!")

    Replay=input("Press Enter key to play again, Enter N to exit. ")
    if Replay=="n" or Replay=="N":
        break