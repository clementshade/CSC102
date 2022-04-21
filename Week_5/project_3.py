import random
lis1 = [0,1,2,3,4,5,6,7,8,9,10]


player_1 = (random.choice(lis1))
player_2 = (random.choice(lis1))

summation = player_1 + player_2

print(summation)

if summation%2 == 0:
    print("even")
else:
    print("odd")
