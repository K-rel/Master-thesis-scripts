from vcScript import *
import vcMatrix 
from vcHelpers.Robot2 import*
import time
import csv
comp = getComponent()
app=getApplication()
robot = app.findComponent("M-20iD/25")
controller = robot.findBehaviour("R-30iB")
VC_counter = comp.getBehaviour("VC_counter")
RB_counter = comp.getBehaviour("RB_counter")
signal = comp.getBehaviour("Boolean Signal")
delay_list = []
RB_cntr_list = []
VC_cntr_list = []
rangeX=0
def OnStart():
  del delay_list[:]
  del RB_cntr_list[:]
  del VC_cntr_list[:]

def MaxMin_delay(x):
  delay_list.append(x)
 
def show_delay():
  print("Max delay time: ", max(delay_list))
  print("Min delay time: ", min(delay_list))
  print("Average delay time: ", sum(delay_list)/len(delay_list))
  exportDelayTimes(delay_list,RB_cntr_list,VC_cntr_list)
  sample_size = 0
def exportDelayTimes(list, RB_list, VC_list):
  rows=[]
  for i in range(len(list)):
    rows.append([i+1,list[i],RB_list[i],VC_list[i]])
  with open("C:\\Users\\karol\\Documents\\VC_delay\\Przypadek_2_delaysTest.csv","w") as file:
    writer=csv.writer(file, lineterminator='\n', delimiter=";")
    writer.writerows(rows)
    
def OnSignal(signal):
  if signal.Value==True:
    resumeRun()
  if signal.Value==False:
    suspendRun()
def OnRun():
  suspendRun()
  sample_size = 0
  while app.Simulation.IsRunning:
    while sample_size<=100:
      if (RB_counter.Value > VC_counter.Value):
        Timer = True
        start=time.clock()
        RB_value = RB_counter.Value
        #print(RB_value)
        #print(VC_counter.Value)
        RB_cntr_list.append(RB_value)
        VC_cntr_list.append(VC_counter.Value)
        while Timer == True:
          if VC_counter.Value == RB_value:
            Timer = False
            end = time.clock()
            #print(end-start)
            MaxMin_delay(end-start)
            sample_size+=1
          else:
            delay(0.0001)
      if (RB_counter.Value < VC_counter.Value):
        Timer = True
        start=time.clock()
        VC_value = VC_counter.Value
        RB_cntr_list.append(RB_counter.Value)
        VC_cntr_list.append(VC_counter.Value)
        while Timer == True:
          if RB_counter.Value == VC_value:
            Timer = False
            end = time.clock()
            #print(start-end)
            MaxMin_delay(start-end)
            sample_size+=1
          else:
            delay(0.0001)
      else:
        delay(0.0001)
    show_delay()
    suspendRun()
    #print("liczniki z 2 skryptu: ",VC_counter.Value, " ",RB_counter.Value)


