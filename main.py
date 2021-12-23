import random

print('Running game...')

winners = 0
losers = 0
loops = 0


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

def determineOutcome(selected_index):
    global doors
    global winners
    global losers

    # is_win = doors[selected_index]['gold']
    is_win = False

    for door in doors:
        if door['selected'] and door['gold']:
            is_win = True
            break;

    print('is_win', is_win)
    print(doors[selected_index])
    print(doors[selected_index]['gold'])

    if is_win:
        winners = winners + 1
        print('winner winner chicken dinner')
    else:
        losers = losers + 1
        print('u suck')

    print(selected_index)
    print(doors)

def getFinalTally():
    print(winners, 'winners')
    print(losers, 'losers')

    winning_percentage = winners / loops

    print(winning_percentage * 100, 'win percantage')


def runGame():
    global loops

    setupDoors()

    selected_index = getRandomDoorIndex()
    doors[selected_index]['selected'] = True

    removeBadDoor()

    selectNewDoor()

    determineOutcome(selected_index)

    resetDoors()

    loops = loops + 1

for _ in range(50):
    runGame()


getFinalTally()






