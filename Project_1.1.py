print()
print("[ WORD PUZZLE GAME ]")
print("Instructions:")
print("-> Make a meaningful word with the letters giving in following question.")
print("-> Every correct answer has 1 score and every wrong answer has -1 score.", end="\n\n")

dict1 = {"father": "RAEHTF", "break": "KABRE", "country": "CYROTNU", "green": "RENEG", "aeroplane":"OAERELANP"}
dict2 = {"programme": "EGMORMARP", "orange": "AENROG", "pineapple": "LPEANIPEP", "leboratory":"YTAOBREOLR", "welcome":"MLOECWE"}
dict3 = {"student": "TUTNDSE", "horse": "ROSHE", "peacock": "CAOECPK", "crocodile":"EDOOIRCCL", "pleasure":"UESLARPE"}
dict4 = {"tiger": "RGIET", "violate": "TOAILVE", "vegetable": "LETGAEBVE", "mountain":"NUTONAMI", "raddish":"HDASRID"}


myList = [dict1, dict2, dict3, dict4]


def wordPuzzle(dictonary):
    i = 1
    score = 0
    for dict_key, dict_value in dictonary.items():
        print(
            "Q{}. Re-aarange and enter the correct word for [ {} ]".format(i, dict_value))
        ans = input()
        if ans.lower() == dict_key:
            print("Wow ! You are genius")
            score +=1
        else:
            print("Oops ! You are wrong")
            score -=1
        i +=1
        print()

    print("Your final score is", score)
    print()
    
 
for data in myList:
    wordPuzzle(data)
    play = input("Do you want to play more (y/n)")
    print()
    if play == "y" or play == "Y":
        pass
    else:
        exit()
    


