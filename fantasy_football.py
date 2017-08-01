import numpy as np
import pandas as pd
import xlsxwriter

player_input = pd.read_excel('/Users/patrickcullinane/PycharmProjects/fantasy_football/Player_input_data.xlsx')

df = pd.DataFrame(np.zeros((len(player_input), 1)))

on_team = df.rename(columns={0:'Is on team'})
is_qb = df.rename(columns={0:'Is QB'})
is_rb = df.rename(columns={0:'Is RB'})
is_wr = df.rename(columns={0:'Is WR'})
is_te = df.rename(columns={0:'Is TE'})
is_k = df.rename(columns={0:'Is K'})
is_d = df.rename(columns={0:'Is D'})

decision = pd.concat([on_team, is_qb, is_rb, is_wr, is_te, is_k, is_d], axis=1)

for i in range(len(decision)):
    i = 0 + i
    position = player_input['Position'].iloc[i]
    #set_pos = pd.DataFrame.set_value(decision, i, ['Is QB'], 1)

    if position == str('QB'):
        decision = pd.DataFrame.set_value(decision, i, ['Is QB'], 1)
    elif player_input['Position'].iloc[i] == str('RB'):
        decision = pd.DataFrame.set_value(decision, i, ['Is RB'], 1)
    elif player_input['Position'].iloc[i] == str('WR'):
        decision = pd.DataFrame.set_value(decision, i, ['Is WR'], 1)
    elif player_input['Position'].iloc[i] == str('TE'):
        decision = pd.DataFrame.set_value(decision, i, ['Is TE'], 1)
    elif player_input['Position'].iloc[i] == str('K'):
        decision = pd.DataFrame.set_value(decision, i, ['Is K'], 1)

full_team = pd.concat([player_input, decision], axis=1)

#sample size
test_team = full_team[0:6]

writer = pd.ExcelWriter('test_team.xlsx', engine='xlsxwriter')
test_team.to_excel(writer, sheet_name='test_team_data')
writer.save()
print('done')

"""
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


val = [60, 100, 120]
wt = [10, 20, 30]
W = 20000
n = len(val)

print(knapSack(W, wt, val, n))

"""



#print(test_team)
