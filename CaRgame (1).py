from Class import State, Player
from utils import InitToNumbers, createVecs, writeSmv,runSmv,writeSmv1,runSmv1, INIT, BOARD_ROWS

import matplotlib.pyplot as plt
import numpy as np

expRate = 0
max_turn = 20
start_q_tabel=0
if __name__ == "__main__":
  x=[]
  x_idx=[]
  colorsx=[]
  y=[] 
  y_idx=[]
  colorsy=[]
  counter1=0
  counter2=0
  for round in range(20):
    #if round >=5 :
        #start_q_tabel=1
    max_games = 2500
    numOfPlayers = int(len(InitToNumbers(ret_type=str)) / 2)
    max_turn = 50
    expRate = 0.3
    pl1 = Player("p1", exp_rate=expRate)
    pl2 = Player("p2", exp_rate=expRate)
    st = State(INIT, pl1, pl2, max_turn,0,start_q_tabel)
    a_v, l_v = createVecs(numOfPlayers, BOARD_ROWS - 1)
    """
    if start_q_tabel==1:
        for i in range(200):
            writeSmv1(numOfPlayers, BOARD_ROWS - 1, pl1, a_v, l_v)
            ans,r=runSmv1()
            pl1.state=ans
            pl1.feedReward(1000)
    """
    res = st.play(max_games, INIT, a_v, l_v, numOfPlayers)
    print(res)
    print("Number of games:", sum(res))
    writeSmv(numOfPlayers, BOARD_ROWS - 1, pl1, a_v, l_v)
    ans, wl_r =runSmv()
    print(ans)
    print("round",round)
    if  st.smv_stop==1:
      y.append(sum(res))
      y_idx.append(round)
      counter1+=1
      if ans=="win":
        colorsy.append("orange")
      else:
        colorsy.append("red")
    else:
      x.append(sum(res))
      x_idx.append(round)
      counter2+=1
      if ans=="win":
        colorsx.append("blue")
      else:
        colorsx.append("purple")
  print("number of times nusmv stops us:",counter1)
  print("number of times convergence stops us:",counter2)
  plt.scatter(x_idx, x,c=colorsx)
  plt.scatter(y_idx, y,c=colorsy)
  plt.show()
