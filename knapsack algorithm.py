import numpy as np
import pandas as pd
import xlsxwriter


player_input = pd.read_excel('/Users/fantasy_football/test_team.xlsx')

player_input = player_input[0:3]

#total budget = W
#number of players = n
#projected score = val
#cost = w

def knapSack(W, wt, val, n):

    if n == 0 or W == 0:
        return 0

    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1))


#val = [60, 100, 120]
#wt = [10, 20, 30]

print(player_input)

val = np.array(player_input['Point Projection'])
wt = np.array(player_input['Cost'])
W = 16000
n = len(val)

print(n)
print(val)
print(wt)
print(wt[n-1])

print(knapSack(W, wt, val, n))

