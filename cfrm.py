import random
import numpy as np
'''
regretSum: A list to keep track of the total regret of each decision
strategy: A list to hold the weightings of each option in a mixed strategy
strategySum: The sum of all the strategies used thus far
oppStrategy: The strategy of a theoretical opponent against whom we must adjust
'''

PASS, BET, NUM_ACTIONS = 0, 1, 2

def main():
    
    regretSum = np.zeros(NUM_ACTIONS)
    strategy = np.zeros(NUM_ACTIONS)
    strategySum = np.zeros(NUM_ACTIONS)




