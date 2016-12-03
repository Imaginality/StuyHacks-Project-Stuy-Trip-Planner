'''
Finds Even Nums in a list.
'''
def even(num):
    return (num%2)==0



def stuyPlan(strtRm,destRm):
    strtFl = 0
    destFl = 0
   
    onehudson = [152, 154]
    onewest = [133, 129, 125]
    twowest = [229, 231]
    twohudson = [233, 235, 237, 239]
    tworiver = [250, 251]
    threeriver = [337, 335, 336, 333, 339]
    threehudson = [350, 351]
    threewest = [325, 327, 329]
    threeeast = [307, 305, 303, 301]
    threecenter = [313, 315]
    foureast = [464, 401, 402, 403, 404, 405, 406, 407]
    fourhudson = [450, 451, 453, 439, 437, 440]
    fourriver = [437, 438, 435, 433]
    fourwest = [433, 432, 431]
    fourcenter= [413, 411]
    fiveeast = [507, 503, 505]
    fivewest = [525]
    fivecenter = [513, 511]
    fiveeast = [507, 505, 503]
    sixhudson = [627,625,634,636,629,638,629,635,640,639]
    sixwest = [615]
    sixcenter = ['library']
#sixeastget data
#sevenhudson = get data
    sevenwest = [727,729,731]
    sevencenter = [717,715]
    seveneast = [709,707,704,705,703]
#eighthudson
    eightwest = [827,829]
    eightcenter = [815,817]
    eighteast = [804,803,807,809,811]
    ninehudson = [935,936, 938, 940, 935, 939, 940]
    ninewest = [927, 926, 936, 931]
#ninecenter get data
#nineeast get data
    teneast = [1010, 1009, 1007, 1006, 1004, 1001]
    tenwest = [1038, 1033, 1024, 1025, 1017]

    cent = eightcenter+sevencenter+sixcenter+fivecenter+fourcenter+threecenter
    west = tenwest+ninewest+eightwest+sevenwest+sixwest+fivewest+fourwest+threewest+twowest+onewest
    east = teneast+eighteast+seveneast+fiveeast+foureast+threeeast
    hudson = ninehudson+sixhudson+fourhudson+threehudson+twohudson+onehudson
    river = fourriver+threeriver+tworiver

    if 99 < strtRm < 200:
        strtFl = 1
    if 200 < strtRm < 300:
        strtFl = 2
    if 300 < strtRm < 400:
        strtFl = 3
    if 400 < strtRm < 500:
        strtFl = 4
    if 500 < strtRm < 600:
        strtFl = 5
    if 600 < strtRm <700:
        strtFl = 6
    if 700 < strtRm < 800:
        strtFl = 7
    if 800 < strtRm < 900:
        strtFl = 8
    if 900 < strtRm < 1000:
        strtFl = 9
    if 1000 < strtRm < 1100:
        strtFl = 10
    if 0 < destRm < 200:
        destFl = 1
    if 200 < destRm < 300:
        destFl = 2
    if 300 < destRm < 400:
        destFl = 3
    if 400 < destRm < 500:
        destFl = 4
    if 500 < destRm < 600:
        destFl = 5
    if 600 < destRm <700:
        destFl = 6
    if 700 < destRm < 800:
        destFl = 7
    if 800 < destRm < 900:
        destFl = 8
    if 900 < destRm < 1000:
        destFl = 9
    if 1000 < destRm < 1100:
        destFl = 10

    if strtFl == destFl:
        return 'Walk'

    if abs(strtFl-destFl) >= 2:
        if strtFl not in [1,10] and destFl not in [1,10]:
            if even(strtFl) == even(destFl):
                return 'Take the Escalator'
            if (strtFl-destFl) > 0:
                if strtRm in west and destRm in hudson:
                   return 'Take Escalator and West Stairwell'
                if strtRm in west and destRm in river:
                   return 'Take Escalator and West Stairwell'
                if destRm in cent:
                   return 'Take Escalator and West Stairwell'
                if destRm in east:
                   return 'Take Escalator and West Stairwell'
                if destRm in west:
                   return 'Take Escalator and West Stairwell'
        if strtRm in east and destRm in hudson:
           return 'Take Escalator and West Stairwell'
        if strtRm in east and destRm in river:
           return 'Take Escalator and East Stairwell'
        if strtRm in east and destRm in cent:
           return 'Take Escalator and East Stairwell'
        if strtRm in east and destRm in east:
           return 'Take Escalator and East Stairwell'
        if strtRm in east and destRm in west:
           return 'Take Escalator and East Stairwell'

    if strtRm in hudson and destRm in (hudson or river): 
        return 'Take Hudson Stairwell'
    if strtRm in hudson and destRm in cent:
        return 'Take Hudson Stairwell'
    if strtRm in hudson and destRm in east:
        return 'Take Hudson Stairwell'
    if strtRm in hudson and destRm in west:
        return 'Take Hudson or West Stairwell'
    if strtRm in river and destRm in hudson:
        return 'Take Hudson Stairwell'
    if strtRm in river and destRm in river:
        return 'Take River Stairwell'
    if strtRm in river and destRm in cent:
        if 99 < destRm < 600:
            return 'Take River Stairwell'
        return 'Take Hudson Stairwell'
    if strtRm in river and destRm in east:
        if 99 < destRm < 600:
            return 'Take River Stairwell'
        return 'Take Hudson Stairwell'
    if strtRm in river and destRm in west:
        if 99 < destRm < 600:
            return 'Take River Stairwell'
        return 'Take Hudson Stairwell'
    if strtRm in west and destRm in hudson:
        return 'Take Hudson Stairwell'
    if strtRm in west and destRm in river:
        return 'Take West Stairwell'
    if strtRm in west and destRm in cent:
        return 'Take West Stairwell'
    if strtRm in west and destRm in east:
        return 'Take West Stairwell'
    if strtRm in west and destRm in west:
        return 'Take West Stairwell'
    if strtRm in east and destRm in hudson:
        return 'Take West Stairwell'
    if strtRm in east and destRm in river:
        return 'Take East Stairwell'
    if strtRm in east and destRm in cent:
        return 'Take East Stairwell'
    if strtRm in east and destRm in east:
        return 'Take East Stairwell'
    if strtRm in east and destRm in west:
        return 'Take East Stairwell'






















