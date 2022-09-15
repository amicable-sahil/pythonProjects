print()
print("[ WORD PUZZLE GAME ]")
print("Instructions:")
print("-> Make a meaningful word with the letters giving in following question.")
print("-> Every correct answer has 1 score and every wrong answer has -1 score.", end="\n\n")

d1 = {"father": "RAEHTF", "break": "KABRE", "country": "CYROTNU", "green": "RENEG", "aeroplane":"OAERELANP"}
d2 = {"programme": "EGMORMARP", "orange": "AENROG", "pineapple": "LPEANIPEP", "leboratory":"YTAOBREOLR", "welcome":"MLOECWE"}
d3 = {"student": "TUTNDSE", "horse": "ROSHE", "peacock": "CAOECPK", "crocodile":"EDOOIRCCL", "pleasure":"UESLARPE"}
d4 = {"tiger": "RGIET", "violate": "TOAILVE", "vegetable": "LETGAEBVE", "mountain":"NUTONAMI", "raddish":"HDASRID"}


myList = [d1, d2, d3, d4]


def fun(dictonary):
    i = 1
    score = 0
    for k, v in dictonary.items():
        print("Q{}. Enter the correct word for [ {} ]".format(i, v))
        ans = input()
        if ans.lower() == k:
            print("You are genius")
            score +=1
        else:
            print("Tum gadhe ho")
            score -=1
        i +=1
        print()

    print("Your final score is", score)
    print()
    
 
for d in myList:
    fun(d)   
    play = input("Do you want to play more (y/n)")
    print()
    if play == "y" or play == "Y":
        pass
    else:
        exit()
    


