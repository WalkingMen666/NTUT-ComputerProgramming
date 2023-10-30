def judge(score1, score2, player1Name, player2Name):
    if(score1 > 10.5): score1 = 0
    if(score2 > 10.5): score2 = 0
    if(score1 == 0): print(player2Name, "Win")
    elif(score1 > score2): print(player1Name, 'Win')
    elif(score1 < score2): print(player2Name, "Win")
    else: print("Tie")
    if(score1 > score2): print(player1Name, 'Win')
    elif(score1 < score2): print(player2Name, 'Win')
    else: print("Tie")

def covert(str):
    if(str =='2'): return 2
    elif(str == '3'): return 3
    elif(str == '4'): return 4
    elif(str == '5'): return 5
    elif(str == '6'): return 6
    elif(str == '7'): return 7
    elif(str == '8'): return 8
    elif(str == '9'): return 9
    elif(str == '10'): return 10
    elif(str == 'A'): return 0.5
    elif(str == 'J'): return 0.5
    elif(str == 'Q'): return 0.5
    elif(str == 'K'): return 0.5    
     
def main():
    player_1_Info = [input() for i in range(4)]
    player_2_Info = [input() for i in range(4)]
    score1, score2 = 0, 0
    for i in range(3): 
        score1 += covert(player_1_Info[i+1])
        score2 += covert(player_2_Info[i+1])
    judge(score1, score2, player_1_Info[0], player_2_Info[0])

main()