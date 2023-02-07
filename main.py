import random

print('Running game...')

first_winners = 0
first_losers = 0
new_door_winners = 0
new_door_losers = 0
loops = 100000


door_one = {
    'gold': False,
    'selected': False,
    'removed': False
}

door_two = {
    'gold': False,
    'selected': False,
    'removed': False
}

door_three = {
    'gold': False,
    'selected': False,
    'removed': False
}

doors = [door_one, door_two, door_three]

def getRandomDoorIndex():
    return random.randint(0, 2)

def setupDoors():
    gold_index = getRandomDoorIndex()
    doors[gold_index]['gold'] = True

def resetDoors():
    global doors
    for i in range(3):
        doors[i] = {
            'gold': False,
            'selected': False,
            'removed': False
        }

def removeBadDoor():
    global doors
    for door in doors:
        if door['gold'] != True and door['selected'] != True:
            door['removed'] = True
            break;

def selectNewDoor():
    global doors
    for door in doors:
        if door['selected'] == True:
            door['selected'] = False
        elif door['selected'] == False and door['removed'] == False:
            door['selected'] = True

def determineOutcome(newDoorSelected):
    global doors
    global first_winners
    global first_losers
    global new_door_winners
    global new_door_losers

    # is_win = doors[selected_index]['gold']
    is_win = False

    for door in doors:
        if door['selected'] and door['gold']:
            is_win = True
            break;

    if is_win:
        if newDoorSelected:
            new_door_winners += 1
        else:
            first_winners = first_winners + 1
    else:
        if newDoorSelected:
            new_door_losers += 1
        else:
            first_losers = first_losers + 1

def getFinalTally():
    print(first_winners, 'Winners while keeping their door')
    print(first_losers, 'Losers while keeping their door')

    first_winning_percentage = (first_winners / loops) * 100

    print('Keeping your door wins', first_winning_percentage, '% of the time')
    print('-----------------------------------')

    print(new_door_winners, 'Winners while choosing a new door')
    print(new_door_losers, 'Losers while choosing a new door')

    new_door_winning_percentage = (new_door_winners / loops) * 100

    print('Choosing a new door wins', new_door_winning_percentage, '% of the time')
    print('-----------------------------------')

def runGame(chooseNewDoor):
    setupDoors()

    selected_index = getRandomDoorIndex()
    doors[selected_index]['selected'] = True

    removeBadDoor()

    if chooseNewDoor:
        selectNewDoor()

    determineOutcome(chooseNewDoor)

    resetDoors()

for _ in range(loops):
    runGame(True)
    runGame(False)


getFinalTally()






