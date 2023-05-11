from random import choice

# the different topics u can choose from
Name = ["SAM", "JOHN", "HARRY"]
Gender = ["BOY", "GIRL", "MALE", "FEMALE"]
Color = ["RED", "BLUE", "GREEN", "YELLOW"]
Sizes = ["SMALL", "MEDIUM", "LARGE"]
Clothes = ["PANTS", "SHIRTS", "SOCKS"]
Currency = ["YEN", "RUPIAH", "DOLLAR", "DONG", "POUND"]

# allocating the topic so we can choose a topic
All_Topics = ["Name", "Gender", "Color", "Sizes", "Clothes", "Currency"]
All_Topics_Dict = {
    "Names":Name,"Gender":Gender,"Color":Color,"Sizes":Sizes,"Clothes":Clothes,"Currency":Currency,
}

# all of the possible actions
def Correct_Guess(P1):
    index = 0
    GC = 0
    for i in Word:
        if P1!=i:
            index +=1
        else:
            Display[index]=i
            index +=1
    
    index = 0
    for Each_Letter in Display:
        if Each_Letter == Word[index]:
            GC += 1
            index +1
        else:
            index +=1
        Unused_Letters.remove(P1)
        return GC

def Already_Guess():
    print("Letter already guessed")

def Invalid_Guess():
    print("Please input letter")

def incorrect_Guess(P1,LL):
    for i in Unused_Letters:
        if P1 == i:
            Unused_Letters.remove(i)
    
    LL -1
    print("Wrong guess u dumbo")
    return LL

while True:
    # choose topics
    Topic = choice(All_Topics)
    for Each_Key in All_Topics_Dict.keys():
        if Topic == Each_Key:
            print("Topic:",Topic)
            Topic = All_Topics_Dict[Each_Key]
            Word = choice(Topic)
            #print(Word)
            print("Word is " +str(len(Word))+" letters long.")
            
    Display = []
    for i in Word:
        Display.append("_")
    print(Display)
    
    Lives_Left = 10
    Guessed_Currently = 0
    Unused_Letters = []
    Valid_Letters = []
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        Unused_Letters.append(i)
        Valid_Letters.append(i)
        
    while Lives_Left != 0 and Guessed_Currently != len(Word):
        P1 = input("Guess here")
        P1 = P1.upper
        if P1 in Word and P1 in Unused_Letters:
            Guessed_Currently = Correct_Guess(P1)
        
        elif P1 not in Valid_Letters:
            Invalid_Guess()
        
        elif P1 in Valid_Letters and P1 in Unused_Letters:
            Already_Guess()
        
        elif P1 in Unused_Letters and P1 not in Word:
            Lives_Left = incorrect_Guess(P1,Lives_Left)
            
        print()
        print(Lives_Left,"Lives Left")
        print(Guessed_Currently, "/", len(Word), "Letters Guessed")
        print(Display)
        
    print()
    if Lives_Left == 0:
        print("word was", Word, ".")
        print("better luck next time bozo")
        
    else:
        print("You got it nice job")

    Replay = input("Press the Enter key to play again, Press N to exit")
    if Replay == "n" or Replay == "N":
        break
    
