Time = 2.0
distance = 50

F_drive_time = 1.4
N_drive_time = 2.5

def speed(D,T):
    velocity = D/T
    velocity = round(velocity)
    print(velocity,"miles per hour.")

speed(distance,Time)

print("Formula one's speed ",end = " ")
speed(distance,F_drive_time)

print("Need for speed's speed",end = " ")
speed(distance,N_drive_time)
