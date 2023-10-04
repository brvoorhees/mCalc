
while True:
    try:
        numplayer = int(input("How many players are there? 2,3,4,5,6: "))
    except ValueError:
        continue
    else:
        if numplayer == 2 or numplayer == 3 or numplayer == 4 or numplayer == 5 or numplayer == 6:
            break
        else:
            continue
playerselect = int(numplayer)
player_list = dict()
num_player = playerselect


while True:
    try:
        gameplay = int(input("PLAY Regular or Fast Dice? 1 = Regular, 2 = Fast: "))
    except ValueError:
        continue
    else:
        if gameplay == 1:
            while num_player > 0:
                playername = input('Player Name ')
                player_list[playername] = 1500
                num_player = num_player - 1
            else:
                print('\n')
                print('Welcome to the game', player_list)
                break

        elif gameplay == 2:
            while num_player > 0:
                playername = input('Player Name ')
                player_list[playername] = 2500
                num_player = num_player - 1
            else:
                print('\n')
                print('Welcome to the game', player_list)
                break
        else:
            continue

def Intro (response, money):
    resint = int(response)

    if resint == 1:
        pmoney = (int(money))
        print('Pass Go')
        tempmoney = 200
        ipmoney = int(tempmoney)
        upmoney = ipmoney + pmoney
        return upmoney
    elif resint == 2:
        pmoney = (int(money))
        question = print('Cost of purchase? Your balance is', pmoney)
        while True:
            try:
                tempmoney = int(input())
            except ValueError:
                print('Cost of purchase? Your balance is', pmoney)
                continue
            else:
                ipmoney = int(tempmoney)
                print('You owe', ipmoney)
                if ipmoney < pmoney:
                    upmoney = pmoney - ipmoney
                    return upmoney
                else:
                    print('You can''t afford this property ')

    elif resint == 5:
        while True:
            try:
                reward = int(input('Reward amount? '))
            except ValueError:
                continue
            else:
                pmoney = (int(money))
                upmoney = pmoney + reward
                return upmoney

    elif resint == 6:
        while True:
            try:
                sellhouses = int(input('Selling houses? (1 = Y/ 2 = N) '))
            except ValueError:
                continue
            else:
                if sellhouses == 1:
                    pmoney = (int(money))
                    while True:
                        try:
                            housecost = int(input('Cost? '))
                        except ValueError:
                            continue
                        else:
                            try:
                                numhouse = int(input('Quantity? '))
                            except ValueError:
                                continue
                            else:
                                pmoneyincrease = housecost * numhouse
                                upmoney = pmoneyincrease + pmoney
                                return upmoney
                                break

                elif sellhouses == 2:
                    try:
                        pmortgage = int(input('Mortgage your property '))
                    except ValueError:
                        continue
                    else:
                        pmoney = int(money)
                        upmoney = pmoney + pmortgage
                        return upmoney
                        break


def pResponse():
    while True:
        try:
            print('\n')
            playresponse = int(input('Select a transaction:\n\n(1) Pass Go\n(2) Purchase Property, Houses, or Hotels\n(3) Pay Another Player\n(4) Penalty\n(5) Reward\n(6) Sell/Mortgage Property\n(7) Quit\n\n'))
        except ValueError:
            continue
        else:
            if playresponse == 1 or playresponse == 2 or playresponse == 3 or playresponse == 4 or playresponse == 5 or playresponse == 6 or playresponse == 7:
                return playresponse
            else:
                continue


def playerTran(type):

        trueplayer = 0
        while trueplayer == 0:
            if type == 'regular':
                playtran = input("Who is making a transaction? ")
                for name in player_list:
                    if name == playtran:
                        return playtran
                    else:
                        continue
            else:
                playtran2 = input('Who do you owe? ')
                for name in player_list:
                    if name == playtran2:
                        return playtran2
                    else:
                        continue

strdone = 7
payanother = 3
penalty = 4
playerResponse = 0
tempmoney = 0
penaltytotal = 0
while playerResponse != strdone:
    type = 'regular'
    ptran = playerTran(type)
    tempmoney = int((player_list.get(ptran)))
    playerResponse = pResponse()
    if playerResponse == 1 or playerResponse == 2 or playerResponse == 5 or playerResponse == 6:
        tempmoney = Intro(playerResponse, tempmoney)            #playermoney = tempmoney
        player_list.pop(ptran)
        player_list.setdefault(ptran, tempmoney)
        print('\n')
        print('Player Totals:')
        print(player_list)
        print('\n')
    elif playerResponse == payanother:
        type = 'pay'
        tempmoney = int((player_list.get(ptran)))
        ptran2 = playerTran(type)
        if ptran != ptran2:
            print('\n')
            print(player_list)
            oweplayermoney = int((player_list.get(ptran2)))
            print('\n')
            while True:
                try:
                    numowe = int(input('How much? '))
                except ValueError:
                    continue
                else:
                    innumowe = int(numowe)
                    tempmoney = tempmoney - innumowe
                    oweplayermoney = oweplayermoney + innumowe
                    player_list.pop(ptran)
                    player_list.setdefault(ptran, tempmoney)
                    player_list.pop(ptran2)
                    player_list.setdefault(ptran2, oweplayermoney)
                    print('\n')
                    print('Player Totals:')
                    print(player_list)
                    print('\n')
                    break
        else:
            print('Can''t pay yourself')
            continue
    elif playerResponse == penalty:
        pmoney = tempmoney
        while True:
            penaltytype = int(input('Paying penalty or Collecting? (1 = Penalty & 2 = Collecting) '))
            if penaltytype == 1:
                try:
                    penaltyamount = int(input('How much? '))
                except ValueError:
                    continue
                else:
                    uppenalty = penaltytotal + penaltyamount
                    penaltytotal = uppenalty
                    upmoney = tempmoney - penaltyamount
                    tempmoney = upmoney
                    player_list.pop(ptran)
                    player_list.setdefault(ptran, tempmoney)
                    print('freeparking total', penaltytotal)
                    print(player_list)
                    print('\n')
                    break
            elif penaltytype == 2:
                tempmoney = tempmoney + penaltytotal
                penaltytotal = 0
                player_list.pop(ptran)
                player_list.setdefault(ptran, tempmoney)
                print(player_list)
                print('\n')
                break
    elif playerResponse == strdone:
        break
