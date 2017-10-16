import sys

# initial values
# Uno
HP = 9094
AT = 43930
DA = 47
TA = 3

el = 1  # DO NOT CHANGE el  element
de = 1  # DO NOT CHANGE de  defense
ed = 1  # DO NOT CHANGE ed  decrease

# Offensive LB
OLBlist = ['attack', 'double', 'triple', 'critical', 'element']
attack = 4      # 500 - 800 - 1000
double = 1      # 3% - 5% - 6%
triple = 0      # 2% - 4% - 5%
critical = 0    # 12% - 20% - 25%
element = 1     # 5% - 8% - 10%

offensive = [0, 0, 0, 0, 0]
maxoffensive = (attack + double + triple + critical + element) * 3

# Defensive LB
DLBlist = ['defense', 'hitpoint', 'decrease']
defense = 3     # 5% - 8% - 10%
hitpoint = 1    # 250 - 500 - 750
decrease = 1    # 2% - 4% - 5%

defensive = [0, 0, 0]
maxdefensive = (defense + hitpoint + decrease) * 3


print("maxoffensive "+str(maxoffensive))
# Offensive
currentpoint = 0

while currentpoint < maxoffensive:
    optimalLB = -1      # kind of optimal LB now
    optimalratio = 0    # increase rate by optimalLB
    optimalLB = 0   # attack

    if offensive[0] < attack:
        optimalratio = 500/AT
    elif offensive[0] < 2*attack:
        optimalratio = 300/AT
    elif offensive[0] < 3*attack:
        optimalratio = 200/AT
    else:   # offensive[0] = attack * 3; fully implied
        optimalratio = 0
        optimalLB = -1

    if double == 0:
        pass
    elif offensive[1] < double:
        ratio = 3/(100 + DA)
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 1
        else:
            pass
    elif offensive[1] < 2*double:
        ratio = 2/(100 + DA)
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 1
        else:
            pass
    elif offensive[1] < 3*double:
        ratio = 1/(100 + DA)
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 1
        else:
            pass
    else:   # fully implied
        pass

    if triple == 0:
        pass
    elif offensive[2] < triple:
        ratio = 4/(100 + 2*TA)
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 2
        else:
            pass
    elif offensive[2] < 2*triple:
        ratio = 4/(100 + 2*TA)
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 2
        else:
            pass
    elif offensive[2] < 3*triple:
        ratio = 2/(100 + 2*TA)
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 2
        else:
            pass
    else:   # fully implied
        pass

    if critical == 0:
        pass
    elif offensive[3] < critical:
        ratio = 0.0144
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 3
        else:
            pass
    elif offensive[3] < 2*critical:
        ratio = 1.04/1.0144 - 1
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 3
        else:
            pass
    elif offensive[3] < 3*critical:
        ratio = 1.0625/1.04 - 1
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 3
        else:
            pass
    else:
        pass

    if element == 0:
        pass
    elif offensive[4] < element:
        ratio = 0.05/el
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 4
        else:
            pass
    elif offensive[4] < 2*element:
        ratio = 0.03/el
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 4
        else:
            pass
    elif offensive[4] < 3*element:
        ratio = 0.02/el
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 4
        else:
            pass
    else:
        pass

    if optimalLB == 0:  # attack
        if offensive[0] < attack:
            AT += 500
        elif offensive[0] < 2*attack:
            AT += 300
        else:
            AT += 200
    elif optimalLB == 1: # double
        if offensive[1] < double:
            DA += 3
        elif offensive[1] < 2*double:
            DA += 2
        else:
            DA += 1
    elif optimalLB == 2: # triple
        if offensive[2] < triple:
            TA += 2
        elif offensive[2] < 2*triple:
            TA += 2
        else:
            TA += 1
    elif optimalLB == 3: # critical
        pass            # independent
    elif optimalLB == 4: # element
        if offensive[4] < element:
            el += 0.05
        elif offensive[4] < element:
            el += 0.03
        else:
            el += 0.02

    offensive[optimalLB] += 1
    currentpoint += 1
    print(OLBlist[optimalLB]+" -> "+str(optimalratio*100)+"% increased")

print("\n")


print("maxdefensive "+str(maxdefensive))
# Defensive
currentpoint = 0

while currentpoint < maxdefensive:
    optimalLB = -1      # kind of optimal LB now
    optimalratio = 0    # increase rate by optimalLB
    optimalLB = 0   # defense

    if defensive[0] < defense:
        optimalratio = 0.05/de
    elif defensive[0] < 2*defense:
        optimalratio = 0.03/de
    elif defensive[0] < 3*defense:
        optimalratio = 0.02/de
    else:
        optimalratio = 0
        optimalLB = -1

    if defensive[1] < hitpoint:
        ratio = 250/HP
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 1
        else:
            pass
    elif defensive[1] < 2*hitpoint:
        ratio = 250/HP
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 1
        else:
            pass
    elif defensive[1] < 3*hitpoint:
        ratio = 250/HP
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 1
        else:
            pass
    else:
        pass

    if defensive[2] < decrease:
        ratio = 2/(98-ed)
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 2
        else:
            pass
    elif defensive[2] < 2*decrease:
        ratio = 2/(98-ed)
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 2
        else:
            pass
    elif defensive[2] < 3*decrease:
        ratio = 1/(99-ed)
        if optimalratio < ratio:
            optimalratio = ratio
            optimalLB = 2
        else:
            pass
    else:
        pass


    if optimalLB == 0:  # defense
        if defensive[0] < defense:
            de += 0.05
        elif defensive[0] < 2*defense:
            de += 0.03
        else:
            de += 0.02
    elif optimalLB == 1: # hitpoint
        if defensive[1] < hitpoint:
            HP += 250
        elif defensive[1] < 2*hitpoint:
            HP += 250
        else:
            HP += 250
    else:                # decrease
        if defensive[2] < decrease:
            ed += 2
        elif defensive[2] < 2*decrease:
            ed += 2
        else:
            ed += 1
        

    defensive[optimalLB] += 1
    currentpoint += 1
    print(DLBlist[optimalLB]+" -> "+str(optimalratio*100)+"% increased")
