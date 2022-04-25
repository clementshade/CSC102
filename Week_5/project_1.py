lis1 = ["hello","bye","care","abc"]


bad_counter = []

print("The words are ",end = "")
print(lis1)
bad_letters = list(str(input("what are your forbidden letter? (e.g \'e\')")))


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
    print(a, correct,"Number of bad letters",num,end = "\n\n")
    bad_counter.append(num)
       
for a in lis1:
    avoids(a)

hard = (min(bad_counter))

least = (bad_counter.index(hard))
print(lis1[least],"has the least number of bad letters")
