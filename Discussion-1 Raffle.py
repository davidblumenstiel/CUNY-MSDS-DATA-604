# -*- coding: utf-8 -*-
"""
Random Raffle

Created on Tue Jun  2 14:17:40 2020

David Blumenstiel
"""

#The raffle simulation
def raffle(Ps,Pm,Pl,Ph,tickets):

    totalWinnings = 0

    import random

    #Sets the values for each type of reward
    smallReward = 10
    medReward = 100
    largeReward = 1000
    hugeReward = 10000
    
    #Runs once for each ticket; adds the total winnings
    for i in range(tickets):
    
        #Bigger rewards perclude smaller ones
        if random.uniform(0, 1) <= Ph:
            totalWinnings += hugeReward
            
        elif random.uniform(0, 1) <= Pl:
            totalWinnings += largeReward
            
        elif random.uniform(0, 1) <= Pm:
            totalWinnings += medReward
            
        elif random.uniform(0, 1) <= Ps:
            totalWinnings += smallReward
            
            
    return totalWinnings


#Defines paramaters we'll be using for the simulations
Ps = .1
Pm = .02
Pl = .005
Ph = .0001
tickets = 20

#Runs the simulation 1000 times
tries = list()
for i in range(1000):
    tries.append(raffle(Ps, Pm, Pl, Ph, tickets))


import statistics
print("Total winnings from all tries: " + str(sum(tries)))
print("Average winnings per try: " + str(statistics.mean(tries)))
print("Average winnings per ticket: " + str(statistics.mean(tries)/tickets))

import matplotlib.pyplot as plt
plt.plot(tries)
plt.xlabel("Raffle Attempt")
plt.ylabel("Raffle Winnings")
plt.show
