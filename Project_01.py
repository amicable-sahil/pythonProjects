print()
print("[ WORD PUZZLE GAME ]")
print("Instructions:")
print("-> Make a meaningful word with the letters giving in following question.")
print("-> Every correct answer has 1 score and every wrong answer has -1 score.", end="\n\n")

score = 0
i = 0
count = 0
word_list = {"Father": "RAEHTF", "Break": "KABRE",
             "Country": "CYROTNU", "Green": "RENEG", "Aeroplane": "OAERELANP", "Mother": "RTEOHM", "Painter": "RIEANPT", "Orange": "GAERON", "Brother": "HOTREBR", "Pineapple": "EPNIPEPAL", "Table": "LABTE", "Policeman": "ENLIMOPCA"}

for correct_word in word_list:  # here 'correct_word' contains the key value of 'word_list'
    if i != 5:
        print("Arrange the given word to make a valid word")
        print(word_list[correct_word])
        ans = input()  # Taking answer from user
        if ans.lower() == correct_word.lower():  # if 'key-value' == answer by user
            print("You are correct")
            score += 1
        else:
            print("You are wrong")
            score -= 1
        i += 1
    else:
        # This condition will execute after every 5 answers
        yes = input("[y/n]")
        if yes == "y":
            print("Arrange the given word to make a valid word")
            print(word_list[correct_word])
            ans = input()
            if ans.lower() == correct_word.lower():
                print("You are correct")
                score += 1
            else:
                print("You are wrong")
                score -= 1
            i = 1
        else:
            break
    count += 1


print()
print("You attempt:", count)
print("Your net score is:", score)
