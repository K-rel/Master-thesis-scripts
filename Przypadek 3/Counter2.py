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
dofs = [j.Dof for j in joints]
executor = robot.findBehaviour("Executor")
signal = comp.getBehaviour("Boolean Signal")
J1_RoboGuide = comp.getBehaviour("RealSignalJ1")
J2_RoboGuide = comp.getBehaviour("RealSignalJ2")
J3_RoboGuide = comp.getBehaviour("RealSignalJ3")
J4_RoboGuide = comp.getBehaviour("RealSignalJ4")
J5_RoboGuide = comp.getBehaviour("RealSignalJ5")
J6_RoboGuide = comp.getBehaviour("RealSignalJ6")
RB_Joints_SPD = comp.getBehaviour("RB_Joints_SPD")

#VC_counter = comp.getBehaviour("VC_counter")
#RB_counter = comp.getBehaviour("RB_counter")
VC_counter = comp.getProperty("Integer_VC")
RB_counter = comp.getProperty("Integer_RB")
VC_Joints_SPD = 5
RBMaxSpeedJ1 = comp.getBehaviour("RBMaxSpeedJ1")
RBMaxSpeedJ2 = comp.getBehaviour("RBMaxSpeedJ2")
RBMaxSpeedJ3 = comp.getBehaviour("RBMaxSpeedJ3")
RBMaxSpeedJ4 = comp.getBehaviour("RBMaxSpeedJ4")
RBMaxSpeedJ5 = comp.getBehaviour("RBMaxSpeedJ5")
RBMaxSpeedJ6 = comp.getBehaviour("RBMaxSpeedJ6")
#joints_speeds=[d.MaxSpeed for d in joints]
posJoints_P1 = [0, 0, 0, 10, 15, 25]
posJoints_P2 = [0, 7, -44, 3, 59, 33]
posJoints_P3 = [42, 28, -38, -43, 64, 70]
posJoints_P4 = [42, 26, 5, -73, 40, 115]


def OnSignal(signal):
  if signal.Value==True:
    resumeRun()
  if signal.Value==False:
    suspendRun()
def OnRun():
  suspendRun()
  counter_RB = 0
  Timer_pos = comp.getBehaviour("timer_pos")
  P1_pos = True
  P2_pos = False
  P3_pos = False
  P4_pos = False
  dT = 0
  while app.Simulation.IsRunning:
    joints_values=[d.VALUE for d in joints]
    #print(joints[5].VALUE)
    #print(joints_speeds[0])
    #print("skrypt 2", RB_counter.Value,VC_counter.Value)
    if (round(J3_RoboGuide.Value) == posJoints_P2[2] and round(J4_RoboGuide.Value) == posJoints_P2[3] and 
        round(J5_RoboGuide.Value) == posJoints_P2[4] and round(J6_RoboGuide.Value) == posJoints_P2[5] and P2_pos==True) or (  
        round(J3_RoboGuide.Value) == posJoints_P1[2] and round(J4_RoboGuide.Value) == posJoints_P1[3] and 
        round(J5_RoboGuide.Value) == posJoints_P1[4] and round(J6_RoboGuide.Value) == posJoints_P1[5] and P1_pos==True) or (round(J5_RoboGuide.Value) == posJoints_P3[4] and round(J6_RoboGuide.Value) == posJoints_P3[5] and P3_pos==True) or (round(J5_RoboGuide.Value) == posJoints_P4[4] and round(J6_RoboGuide.Value) == posJoints_P4[5] and P4_pos==True):
      counter_RB = counter_RB+1
      RB_counter.Value = counter_RB
      Timer_pos.Value = True
      if P1_pos == True and P2_pos == False and P3_pos == False and P4_pos == False:
        P1_pos = False
        P2_pos = True
        P3_pos = False
        P4_pos = False
      elif P1_pos == False and P2_pos == True and P3_pos == False and P4_pos == False:
        P1_pos = False
        P2_pos = False
        P3_pos = True
        P4_pos = False
      elif P1_pos == False and P2_pos == False and P3_pos == True and P4_pos == False:
        P1_pos = False
        P2_pos = False
        P3_pos = False
        P4_pos = True
      else:
        P1_pos = True
        P2_pos = False
        P3_pos = False
        P4_pos = False
    delay(0.0001)
    #RB_test2 = J1_RoboGuide.Value
    #print(abs(RB_test1-RB_test2)*10)



