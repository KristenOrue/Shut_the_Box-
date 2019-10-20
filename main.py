from random import randint

print("Let's Play SHUT THE BOX!!\n")

#Display the Box
flaps = ["1","2","3","4","5","6","7","8","9"]
print(*flaps, sep='|', end='| ')

#Roll your dice
die_1, die_2 = randint(1,6), randint(1,6)

print("\n")
print('Current Roll:', die_1,',',die_2)

#Enter flaps to flip
takeTurn = input('Enter the flaps you with to flip seperated by a space (q to quit): ')

if takeTurn in flaps:
    replace = flaps.index(takeTurn)
    flaps.pop(replace)
    flaps.insert(replace, ".")
    print("\n")
    print(*flaps, sep='|', end='| ')
if flaps == ['.','.','.','.','.','.','.','.','.','.']:
    print('YOU WIN!!')


# def quit(string):
#         if variable == 'q':
#             return True

# def take_a_chance(flaps, printGame):
#     #If there are no more flaps left YOU'VE WON!
#     if not flaps: return True

#     for flap in flaps:
#         if flap == variable:
#             flaps.remove(flap)
#             return display_the_box()


