from vcScript import *
import vcMatrix 
from vcHelpers.Robot2 import*
import time
import csv
comp = getComponent()
app=getApplication()
robot = app.findComponent("M-20iD/25")
controller = robot.findBehaviour("R-30iB")
joints = controller.Joints
signal = comp.getBehaviour("Boolean Signal")
joints_speeds=[d.MaxSpeed for d in joints]
J1SpeedsList = []
J2SpeedsList = []
J3SpeedsList = []
J4SpeedsList = []
J5SpeedsList = []
J6SpeedsList = []
timeList=[]

def OnStart():
  del J1SpeedsList[:]
  del J2SpeedsList[:]
  del J3SpeedsList[:]
  del J4SpeedsList[:]
  del J5SpeedsList[:]
  del J6SpeedsList[:]
  del timeList[:]

def Append_Fun(J1,J2,J3,J4,J5,J6,T):
  J1SpeedsList.append(J1)
  J2SpeedsList.append(J2)
  J3SpeedsList.append(J3)
  J4SpeedsList.append(J4)
  J5SpeedsList.append(J5)
  J6SpeedsList.append(J6)
  timeList.append(T)
def sendLists():
  exportLists(J1SpeedsList,J2SpeedsList,J3SpeedsList,J4SpeedsList,J5SpeedsList,J6SpeedsList,timeList)
def exportLists(J1,J2,J3,J4,J5,J6,T):
  print("wyeksportowano listy")
  rows=[]
  for i in range(len(T)):
    rows.append([J1[i],J2[i],J3[i],J4[i],J5[i],J6[i],T[i]])
  with open("C:\\Users\\karol\\Documents\\VC_delay\\JointsSpeedPrzyp2.csv","w") as file:
    writer=csv.writer(file, lineterminator='\n', delimiter=";")
    writer.writerows(rows)
    

def OnSignal(signal):
  if signal.Value==True:
    resumeRun()
  if signal.Value==False:
    suspendRun()

def OnRun():
  #suspendRun()
  sample_size = 0
  time = 0
  while app.Simulation.IsRunning:
    while sample_size<=500:
      print(joints[0].MaxSpeed)
      print(joints[1].MaxSpeed)
      print(joints[2].MaxSpeed)
      print(joints[3].MaxSpeed)
      print(joints[4].MaxSpeed)
      print(joints[5].MaxSpeed)
      Append_Fun(joints[0].MaxSpeed,joints[1].MaxSpeed,joints[2].MaxSpeed,joints[3].MaxSpeed,joints[4].MaxSpeed,joints[5].MaxSpeed,time)
      delay(0.25)
      time+=0.25
      sample_size+=1
    sendLists()
  pass


