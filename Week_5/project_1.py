lis1 = ["hello","bye","care","abc"]
bad_counter = []

bad_letters = list(str(input("what are your forbidden letter? (e.g asrwsd)")))


def avoids(a):
    num = 0
    correct = True
    word = a 
    for i in list(word):
        if i in bad_letters:
           # print("no")
            correct = False
            num += 1
        else:
            pass
           # print("yes")
    print(a, correct,num," bad letters")
    bad_counter.append(num)
       
for a in lis1:
    avoids(a)

print(bad_counter)

hard = (min(bad_counter))
print(bad_counter.index(hard))
