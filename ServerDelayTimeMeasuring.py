from vcScript import *
import time
import csv
import os.path
from itertools import izip
SAMPLING_INTERVAL = 0.0001
sample_size = 1000

def OnStart():
  del delay_list[:]

def getRobotJointValues():
  joint_values = [d.VALUE for d in joints]
  return joint_values


def stopRecordingJointValues(program_executor):
  suspendRun()
  
  
def getLagTime():
  lag_times = [d.LagTime for d in dofs]
  return lag_times
  
def getJ7_Value():
  J7_Value=joints[6].VALUE=joints[6].VALUE+1
  return J7_Value
 
def getJ8_Value():
  J8_Value=joints[7].VALUE
  return J8_Value
def MaxMin_delay(x):
  delay_list.append(x)
def show_delay():
  
  print("Max delay time: ", max(delay_list))
  print("Min delay time: ", min(delay_list))
  print("Average delay time: ", sum(delay_list)/len(delay_list))
  exportDelayTimes(delay_list)
  
def exportDelayTimes(list):
  rows=[]
  for i in range(sample_size):
    rows.append([i+1,list[i]])
  with open("C:\\Users\\karol\\Documents\\VC_delay\\delays.csv","w") as file:
    writer=csv.writer(file, lineterminator='\n', delimiter=";")
    writer.writerows(rows)
    
def OnRun():
  while app.Simulation.IsRunning:
    for i in range(sample_size):
      start=time.clock()
      J7_value = getJ7_Value()
      wU=True
      while wU == True:
        if getJ8_Value() == J7_value:
          wU = False
        else:
          delay(SAMPLING_INTERVAL)
      end = time.clock()
      print((end-start)/2)
      MaxMin_delay((end-start)/2)
    show_delay()
    suspendRun()
  pass

comp = getComponent()
app = getApplication()
robot = app.findComponent("M-20iD/25")
controller = robot.findBehaviour("R-30iB")
delay_list = []
joints = controller.Joints
dofs = [j.Dof for j in joints]
executor = robot.findBehaviour("Executor")
executor.OnProgramFinished = stopRecordingJointValues